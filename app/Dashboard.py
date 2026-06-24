"""
Vancouver Property Value Prediction — Streamlit App
Main entry point: project overview and navigation.
"""

import sys
from pathlib import Path

# Add app and root to path so pages can import from src/
_ROOT = Path(__file__).resolve().parent.parent
_APP = Path(__file__).resolve().parent
sys.path.insert(0, str(_ROOT))
sys.path.insert(0, str(_APP))

import streamlit as st
from language_utils import language_selector, tr

# ============================================================
# Page configuration
# ============================================================
st.set_page_config(
    page_title="Vancouver Property Predictor",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/racarrillo2/vancouver-property-value-prediction',
        'Report a bug': 'https://github.com/racarrillo2/vancouver-property-value-prediction/issues',
        'About': 'Vancouver Property Value Prediction — ML portfolio project by Rafael Carrillo Mirabal'
    }
)

# ============================================================
# Sidebar
# ============================================================
language_selector()  # Must be first

with st.sidebar:
    st.title(tr("sidebar_title"))
    st.caption(tr("sidebar_caption"))
    st.divider()
    st.markdown(tr("sidebar_navigate"))
    st.divider()
    st.caption(tr("sidebar_built_by"))
    st.caption("[GitHub](https://github.com/racarrillo2/vancouver-property-value-prediction) · [LinkedIn](https://www.linkedin.com/in/rafael-carrillo-mirabal/?locale=en)")

# ============================================================
# Main content
# ============================================================
st.title(tr("home_title"))
st.markdown(tr("home_subtitle"))

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric(tr("metric_r2"), "0.80")
col2.metric(tr("metric_mae"), "$376K")
col3.metric(tr("metric_mape"), "15.6%")
col4.metric(tr("metric_training"), tr("metric_training_value"))
col5.metric(tr("metric_cv"), "0.003")

st.divider()

col_left, col_right = st.columns(2)

with col_left:
    st.subheader(tr("home_problem_title"))
    st.markdown(tr("home_problem_text"))

    st.subheader(tr("home_data_title"))
    st.markdown(tr("home_data_text"))

with col_right:
    st.subheader(tr("home_tech_title"))
    st.markdown(tr("home_tech_text"))

    st.subheader(tr("home_what_title"))
    st.markdown(tr("home_what_text"))

st.divider()
st.info(tr("home_disclaimer"), icon="ℹ️")