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

from language_utils import language_selector, tr
from src.data_utils import load_processed_data

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

    choropleth = folium.Choropleth(
        geo_data=_geojson,
        name="choropleth",
        data=_agg_data,
        columns=["geo_name", "median_value"],
        key_on="feature.properties.name",
        fill_color="YlOrRd",
        fill_opacity=0.7,
        line_opacity=0.3,
        legend_name=tr("map_legend_title"),
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
                f"Range: ${r['min_value']:,.0f} – ${r['max_value']:,.0f}"
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
st.title(tr("map_title"))
st.markdown(tr("map_subtitle"))

col_filter, _ = st.columns([3, 7])
with col_filter:
    legal_type = st.selectbox(
        tr("map_filter_legal"),
        options=["ALL", "STRATA", "LAND"],
        format_func=lambda x: tr("map_filter_all") if x == "ALL" else x,
    )

agg_data, mapped_count, unmapped_count = prepare_map_data(legal_type)

tab_map, tab_data = st.tabs([tr("map_tab_map"), tr("map_tab_data")])

with tab_map:
    m = build_map(agg_data, load_geojson())
    st_folium(m, use_container_width=True, height=600)

    st.caption(
        f"✅ {mapped_count:,.0f} {tr('map_mapped')} &nbsp;·&nbsp; "
        f"ℹ️ {unmapped_count:,.0f} {tr('map_unmapped')}"
    )
    st.info(tr("map_note"), icon="ℹ️")

with tab_data:
    lang = st.session_state.get("lang", "en")
    display_df = agg_data.rename(
        columns={
            "geo_name": tr("map_neighbourhood"),
            "median_value": tr("map_median_value"),
            "count": tr("map_property_count"),
        }
    )
    display_df[tr("map_median_value")] = display_df[tr("map_median_value")].apply(
        lambda x: f"${x:,.0f}"
    )
    st.dataframe(
        display_df.sort_values(tr("map_median_value"), ascending=False),
        use_container_width=True,
        hide_index=True,
    )
