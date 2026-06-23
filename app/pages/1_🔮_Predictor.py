"""
Predictor page — interactive form to estimate property values.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))          # app/
sys.path.insert(0, str(Path(__file__).parent.parent.parent))   # root

import streamlit as st
import pandas as pd
import numpy as np
from language_utils import language_selector, tr, get_lang
from translations import display_value, LEGAL_TYPE_DISPLAY, ZONING_DISPLAY
from src.model_utils import load_model_and_metadata
from src.config import CURRENT_YEAR, MAE

# ============================================================
# Page config
# ============================================================
st.set_page_config(page_title="Predictor", page_icon="🔮", layout="wide")

# Sidebar language selector
language_selector()

# ============================================================
# Load model and metadata
# ============================================================
@st.cache_resource
def get_model_and_metadata():
    return load_model_and_metadata()

try:
    model, metadata = get_model_and_metadata()
except FileNotFoundError as e:
    st.error(f"⚠️ Model files not found.\n\n{e}")
    st.stop()

# ============================================================
# Header
# ============================================================
st.title(tr("pred_title"))
st.markdown(tr("pred_subtitle"))
st.divider()

# ============================================================
# Form
# ============================================================
col1, col2 = st.columns(2)

with col1:
    st.subheader(tr("pred_location_section"))

    neighbourhood = st.selectbox(
        tr("pred_neighbourhood"),
        options=metadata['neighbourhoods'],
        index=metadata['neighbourhoods'].index('Shaughnessy') if 'Shaughnessy' in metadata['neighbourhoods'] else 0,
        help=tr("pred_neighbourhood_help")
    )

    legal_type = st.selectbox(
    tr("pred_legal_type"),
    options=metadata['legal_types'],
    format_func=lambda x: display_value(x, LEGAL_TYPE_DISPLAY, get_lang()),
    help=tr("pred_legal_type_help")
    )

    zoning = st.selectbox(
    tr("pred_zoning"),
    options=metadata['zoning_classifications'],
    format_func=lambda x: display_value(x, ZONING_DISPLAY, get_lang()),
    help=tr("pred_zoning_help")
    )

with col2:
    st.subheader(tr("pred_characteristics_section"))

    year_built = st.slider(
        tr("pred_year_built"),
        min_value=1900, max_value=2026, value=2000, step=1,
        help=tr("pred_year_built_help")
    )

    year_improved = st.slider(
        tr("pred_year_improved"),
        min_value=1900, max_value=2026, value=year_built, step=1,
        help=tr("pred_year_improved_help")
    )

# Calculated features
property_age = CURRENT_YEAR - year_built
years_since_improvement = CURRENT_YEAR - year_improved

st.divider()
col_a, col_b = st.columns(2)
col_a.info(tr("pred_age_info", years=property_age))
col_b.info(tr("pred_improvement_info", years=years_since_improvement))

# ============================================================
# Prediction
# ============================================================
st.divider()
predict_button = st.button(tr("pred_button"), type="primary", use_container_width=True)

if predict_button:
    input_data = pd.DataFrame({
        'property_age': [property_age],
        'years_since_improvement': [years_since_improvement],
        'neighbourhood_name': [neighbourhood],
        'legal_type': [legal_type],
        'zoning_classification': [zoning]
    })

    log_prediction = model.predict(input_data)[0]
    prediction_dollars = np.expm1(log_prediction)

    mae = MAE
    lower_bound = max(0, prediction_dollars - mae)
    upper_bound = prediction_dollars + mae

    st.divider()
    st.subheader(tr("pred_result_title"))

    col_main, col_range = st.columns([2, 1])
    col_main.metric(tr("pred_predicted_label"), f"${prediction_dollars:,.0f} CAD")
    col_range.metric(tr("pred_range_label"), f"${lower_bound:,.0f} — ${upper_bound:,.0f}")

    st.markdown(tr("pred_explanation",
                   age=property_age,
                   legal_type=legal_type,
                   neighbourhood=neighbourhood,
                   zoning=zoning,
                   value=prediction_dollars))

    if prediction_dollars > 5_000_000:
        st.warning(tr("pred_luxury_warning"), icon="⚠️")

st.divider()
st.caption(tr("pred_footer"))