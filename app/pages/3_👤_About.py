"""
About page — project context, author info, and links.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import streamlit as st
from language_utils import language_selector, tr

st.set_page_config(page_title="About", page_icon="👤", layout="wide")
language_selector()

st.title(tr("about_title"))
st.divider()

st.header(tr("about_project_title"))
st.markdown(tr("about_project_text"))

st.divider()
st.header(tr("about_author_title"))

col1, col2 = st.columns([1, 2])
with col1:
    st.markdown("### Rafael Carrillo Mirabal")
    st.markdown(tr("about_location"))
    st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/rafael-carrillo-mirabal/?locale=en)")
    st.markdown("[💻 GitHub](https://github.com/racarrillo2)")

with col2:
    st.markdown(tr("about_bio"))

st.divider()
st.header(tr("about_tech_title"))

col_a, col_b = st.columns(2)
with col_a:
    st.subheader(tr("about_data_subtitle"))
    st.markdown(tr("about_data_text"))
    st.subheader(tr("about_model_subtitle"))
    st.markdown(tr("about_model_text"))

with col_b:
    st.subheader(tr("about_perf_subtitle"))
    st.markdown(tr("about_perf_text"))
    st.subheader(tr("about_limits_subtitle"))
    st.markdown(tr("about_limits_text"))

st.divider()
st.header(tr("about_links_title"))

col_x, col_y, col_z = st.columns(3)
with col_x:
    st.link_button(tr("about_link_code"), "https://github.com/racarrillo2/vancouver-property-value-prediction", use_container_width=True)
with col_y:
    st.link_button(tr("about_link_linkedin"), "https://www.linkedin.com/in/rafael-carrillo-mirabal/?locale=en", use_container_width=True)
with col_z:
    st.link_button(tr("about_link_data"), "https://opendata.vancouver.ca/explore/dataset/property-tax-report/", use_container_width=True)

st.divider()
st.caption(tr("about_footer"))