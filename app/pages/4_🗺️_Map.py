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
from streamlit_folium import st_folium

from language_utils import language_selector, get_lang
from src.data_utils import load_processed_data

_TEXTS = {
    "title": {"en": "Vancouver Property Map", "es": "Mapa de Propiedades Vancouver"},
    "subtitle": {
        "en": "Median property value by neighbourhood. Darker = higher value.",
        "es": "Valor mediano de propiedad por barrio. Mas oscuro = mayor valor.",
    },
    "filter_legal": {"en": "Filter by legal type", "es": "Filtrar por tipo legal"},
    "filter_all": {"en": "All properties", "es": "Todas las propiedades"},
    "tab_map": {"en": "Map", "es": "Mapa"},
    "tab_data": {"en": "Data", "es": "Datos"},
    "neighbourhood": {"en": "Neighbourhood", "es": "Barrio"},
    "median_value": {"en": "Median value", "es": "Valor mediano"},
    "property_count": {"en": "Properties", "es": "Propiedades"},
    "mapped": {
        "en": "properties mapped",
        "es": "propiedades mapeadas",
    },
    "unmapped": {
        "en": "not mapped (sub-neighbourhoods)",
        "es": "no mapeadas (sub-areas)",
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
        )
        .round(0)
        .reset_index()
    )

    return agg, mapped.sum(), (~mapped).sum()


@st.cache_resource
def build_map(_agg_data, _geojson):
    value_map = {
        row["geo_name"]: row["median_value"] for _, row in _agg_data.iterrows()
    }
    all_values = [v for v in value_map.values() if pd.notna(v)]
    if not all_values:
        vmin, vmax = 0, 1
    else:
        vmin, vmax = min(all_values), max(all_values)

    def style_fn(feature):
        name = feature["properties"]["name"]
        val = value_map.get(name)
        if val is None or pd.isna(val):
            return {
                "fillColor": "#f0f0f0",
                "color": "#b0b0b0",
                "weight": 0.5,
                "fillOpacity": 0.5,
            }
        ratio = (val - vmin) / (vmax - vmin) if vmax > vmin else 0.5
        r = int(255 * (1 - ratio))
        g = int(255 * (1 - ratio * 0.6))
        b = int(255 * (1 - ratio * 0.8))
        return {
            "fillColor": f"#{r:02x}{g:02x}{b:02x}",
            "color": "#333333",
            "weight": 0.8,
            "fillOpacity": 0.75,
        }

    m = folium.Map(
        location=[49.25, -123.12],
        zoom_start=11,
        tiles="OpenStreetMap",
        control_scale=True,
    )

    for feature in _geojson["features"]:
        name = feature["properties"]["name"]
        row = _agg_data[_agg_data["geo_name"] == name]
        if not row.empty:
            r = row.iloc[0]
            tip = (
                f"<b>{name}</b><br>"
                f"Median: ${r['median_value']:,.0f}<br>"
                f"Mean: ${r['mean_value']:,.0f}<br>"
                f"Properties: {r['count']:,.0f}"
            )
        else:
            tip = f"<b>{name}</b><br>No data"
        folium.GeoJson(
            feature,
            style_function=style_fn,
            tooltip=tip,
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
    try:
        m = build_map(agg_data, load_geojson())
        st_folium(m, width=900, height=600)
    except Exception as e:
        st.error(f"Map error: {e}")

    st.caption(
        f"{mapped_count:,.0f} {txt('mapped')} | "
        f"{unmapped_count:,.0f} {txt('unmapped')}"
    )

with tab_data:
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
    cols = [txt("neighbourhood"), txt("property_count"), txt("median_value")]
    remaining = [c for c in display_df.columns if c not in cols]
    st.dataframe(
        display_df[cols + remaining],
        use_container_width=True,
        hide_index=True,
    )
