"""
Map page — interactive choropleth of property values across Vancouver neighbourhoods.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import json

import folium
import pandas as pd
import streamlit as st
from folium.plugins import Fullscreen
from streamlit_folium import st_folium

from language_utils import language_selector, get_lang
from src.data_utils import load_processed_data

_TEXTS = {
    "title": {"en": "Vancouver Property Map", "es": "Mapa de Propiedades Vancouver"},
    "subtitle": {
        "en": "Explore median property values across Vancouver neighbourhoods. Darker areas indicate higher prices.",
        "es": "Explora los valores medios de propiedades por barrio. Las areas mas oscuras indican precios mas altos.",
    },
    "filter_legal": {"en": "Filter by legal type", "es": "Filtrar por tipo legal"},
    "filter_all": {"en": "All properties", "es": "Todas las propiedades"},
    "legend_title": {"en": "Median value (CAD)", "es": "Valor mediano (CAD)"},
    "tab_map": {"en": "Map", "es": "Mapa"},
    "tab_data": {"en": "Neighbourhood data", "es": "Datos por barrio"},
    "neighbourhood": {"en": "Neighbourhood", "es": "Barrio"},
    "median_value": {"en": "Median value", "es": "Valor mediano"},
    "property_count": {"en": "Properties", "es": "Propiedades"},
    "mapped": {
        "en": "properties mapped to official boundaries",
        "es": "propiedades mapeadas a limites oficiales",
    },
    "unmapped": {
        "en": "properties not mapped (sub-neighbourhoods under parent areas)",
        "es": "propiedades no mapeadas (sub-areas agrupadas en barrios padres)",
    },
    "note": {
        "en": "**Note:** Some neighbourhoods in the data (e.g., Coal Harbour, Yaletown, False Creek) are sub-districts within larger City of Vancouver official boundaries. Properties in those areas are grouped into their parent neighbourhood for mapping.",
        "es": "**Nota:** Algunos barrios en los datos (ej. Coal Harbour, Yaletown, False Creek) son sub-areas dentro de los limites oficiales de Vancouver. Las propiedades en esas areas se agrupan en el barrio padre para el mapa.",
    },
}


def txt(key):
    lang = get_lang()
    return _TEXTS.get(key, {}).get(lang, _TEXTS.get(key, {}).get("en", key))


st.set_page_config(page_title="Property Map", page_icon="🗺️", layout="wide")
language_selector()

GEOJSON_PATH = (
    Path(__file__).parent.parent.parent
    / "data"
    / "raw"
    / "local-area-boundary.geojson"
)

NEIGHBOURHOOD_MAP = {
    "Arbutus-Ridge": "Arbutus Ridge",
    "Champlain Heights": "Victoria-Fraserview",
    "Coal Harbour": "West End",
    "Downtown / West End": "West End",
    "East Hastings": "Strathcona",
    "False Creek": "Fairview",
    "First Shaughnessy": "Shaughnessy",
    "Joyce": "Renfrew-Collingwood",
    "Other / Mixed": None,
    "Renfrew": "Renfrew-Collingwood",
    "Yaletown": "Downtown",
}


@st.cache_resource
def load_geojson():
    with open(GEOJSON_PATH, "r") as f:
        return json.load(f)


@st.cache_data
def get_geo_names(_geojson):
    return {f["properties"]["name"] for f in _geojson["features"]}


def map_neighbourhood(name, geo_names):
    if pd.isna(name):
        return None
    name = name.strip()
    if name in geo_names:
        return name
    if name in NEIGHBOURHOOD_MAP:
        return NEIGHBOURHOOD_MAP[name]
    alt = name.replace("-", " ")
    if alt in geo_names:
        return alt
    return None


@st.cache_data
def prepare_map_data(legal_type_filter=None):
    df = load_processed_data()
    geojson = load_geojson()
    geo_names = get_geo_names(geojson)

    df["geo_name"] = df["neighbourhood_name"].apply(
        lambda x: map_neighbourhood(x, geo_names)
    )

    if legal_type_filter and legal_type_filter != "ALL":
        df = df[df["legal_type"] == legal_type_filter]

    mapped = df["geo_name"].notna()
    agg = (
        df[mapped]
        .groupby("geo_name")
        .agg(
            count=("total_value", "count"),
            median_value=("total_value", "median"),
            mean_value=("total_value", "mean"),
            min_value=("total_value", "min"),
            max_value=("total_value", "max"),
        )
        .round(0)
        .reset_index()
    )
    agg.columns = [
        "geo_name",
        "count",
        "median_value",
        "mean_value",
        "min_value",
        "max_value",
    ]

    mapped_count = mapped.sum()
    unmapped_count = (~mapped).sum()

    return agg, mapped_count, unmapped_count


@st.cache_resource
def build_map(_agg_data, _geojson):
    m = folium.Map(
        location=[49.25, -123.12],
        zoom_start=12,
        tiles="CartoDB positron",
        control_scale=True,
    )
    Fullscreen().add_to(m)

    folium.Choropleth(
        geo_data=_geojson,
        name="choropleth",
        data=_agg_data,
        columns=["geo_name", "median_value"],
        key_on="feature.properties.name",
        fill_color="YlOrRd",
        fill_opacity=0.7,
        line_opacity=0.3,
        legend_name=txt("legend_title"),
        highlight=True,
        bins=7,
    ).add_to(m)

    for feature in _geojson["features"]:
        name = feature["properties"]["name"]
        row = _agg_data[_agg_data["geo_name"] == name]
        if not row.empty:
            r = row.iloc[0]
            tooltip_text = (
                f"<b>{name}</b><br>"
                f"Median: ${r['median_value']:,.0f}<br>"
                f"Mean: ${r['mean_value']:,.0f}<br>"
                f"Properties: {r['count']:,.0f}<br>"
                f"Range: ${r['min_value']:,.0f} - ${r['max_value']:,.0f}"
            )
        else:
            tooltip_text = f"<b>{name}</b><br>No data"
        folium.GeoJson(
            feature,
            style_function=lambda x: {
                "fillOpacity": 0,
                "weight": 0.5,
                "color": "gray",
                "fillColor": "transparent",
            },
            tooltip=tooltip_text,
        ).add_to(m)

    return m


# ============================================================
# Page layout
# ============================================================
st.title(txt("title"))
st.markdown(txt("subtitle"))

col_filter, _ = st.columns([3, 7])
with col_filter:
    legal_type = st.selectbox(
        txt("filter_legal"),
        options=["ALL", "STRATA", "LAND"],
        format_func=lambda x: txt("filter_all") if x == "ALL" else x,
    )

agg_data, mapped_count, unmapped_count = prepare_map_data(legal_type)

tab_map, tab_data = st.tabs([txt("tab_map"), txt("tab_data")])

with tab_map:
    m = build_map(agg_data, load_geojson())
    st_folium(m, use_container_width=True, height=600)

    st.caption(
        f"{mapped_count:,.0f} {txt('mapped')}  |  "
        f"{unmapped_count:,.0f} {txt('unmapped')}"
    )
    st.info(txt("note"), icon=None)

with tab_data:
    lang = get_lang()
    display_df = agg_data.rename(
        columns={
            "geo_name": txt("neighbourhood"),
            "median_value": txt("median_value"),
            "count": txt("property_count"),
        }
    )
    display_df[txt("median_value")] = display_df[txt("median_value")].apply(
        lambda x: f"${x:,.0f}"
    )
    col_order = [txt("neighbourhood"), txt("property_count"), txt("median_value")]
    remaining = [c for c in display_df.columns if c not in col_order]
    st.dataframe(
        display_df[col_order + remaining],
        use_container_width=True,
        hide_index=True,
    )
