"""
Predictor page — interactive form to estimate property values.
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib
from pathlib import Path

# ============================================================
# Page config
# ============================================================
st.set_page_config(page_title="Predictor", page_icon="🔮", layout="wide")

# ============================================================
# Load model and metadata (cached so it loads only once)
# ============================================================
@st.cache_resource
def load_model_and_metadata():
    model_path = Path(__file__).parent.parent.parent / "models" / "best_model.pkl"
    metadata_path = Path(__file__).parent.parent.parent / "models" / "model_metadata.pkl"
    model = joblib.load(model_path)
    metadata = joblib.load(metadata_path)
    return model, metadata

try:
    model, metadata = load_model_and_metadata()
except FileNotFoundError as e:
    st.error(f"⚠️ Model files not found. Make sure `models/best_model.pkl` and `models/model_metadata.pkl` exist.\n\n{e}")
    st.stop()

# ============================================================
# Header
# ============================================================
st.title("🔮 Property Value Predictor")
st.markdown(
    "Enter the characteristics of a Vancouver property to get an estimated market value."
)
st.divider()

# ============================================================
# Form layout (two columns)
# ============================================================
col1, col2 = st.columns(2)

with col1:
    st.subheader("📍 Location & type")

    neighbourhood = st.selectbox(
        "Neighbourhood",
        options=metadata['neighbourhoods'],
        index=metadata['neighbourhoods'].index('Shaughnessy') if 'Shaughnessy' in metadata['neighbourhoods'] else 0,
        help="The Vancouver neighbourhood where the property is located."
    )

    legal_type = st.selectbox(
        "Legal type",
        options=metadata['legal_types'],
        help="STRATA = condo/apartment unit. LAND = full land ownership (house, lot)."
    )

    zoning = st.selectbox(
        "Zoning classification",
        options=metadata['zoning_classifications'],
        help="The zoning category assigned by the City of Vancouver."
    )

with col2:
    st.subheader("🏗️ Property characteristics")

    year_built = st.slider(
        "Year built",
        min_value=1900,
        max_value=2026,
        value=2000,
        step=1,
        help="The year the property was originally constructed."
    )

    year_improved = st.slider(
        "Year of last major improvement (renovation)",
        min_value=1900,
        max_value=2026,
        value=year_built,
        step=1,
        help="The year of the most recent significant renovation. If never renovated, set equal to year built."
    )

# Calculated features
CURRENT_YEAR = 2026
property_age = CURRENT_YEAR - year_built
years_since_improvement = CURRENT_YEAR - year_improved

# Show calculated values
st.divider()
col_a, col_b = st.columns(2)
col_a.info(f"**Property age:** {property_age} years")
col_b.info(f"**Years since last improvement:** {years_since_improvement} years")

# ============================================================
# Prediction button
# ============================================================
st.divider()
predict_button = st.button("🔮 Predict property value", type="primary", use_container_width=True)

if predict_button:
    # Build input row matching training schema
    input_data = pd.DataFrame({
        'property_age': [property_age],
        'years_since_improvement': [years_since_improvement],
        'neighbourhood_name': [neighbourhood],
        'legal_type': [legal_type],
        'zoning_classification': [zoning]
    })

    # Predict (model output is log-transformed, we invert with expm1)
    log_prediction = model.predict(input_data)[0]
    prediction_dollars = np.expm1(log_prediction)

    # Confidence interval based on test MAE
    mae = 376432
    lower_bound = max(0, prediction_dollars - mae)
    upper_bound = prediction_dollars + mae

    # ============================================================
    # Show prediction
    # ============================================================
    st.divider()
    st.subheader("💰 Estimated value")

    col_main, col_range = st.columns([2, 1])

    with col_main:
        st.metric(
            label="Predicted property value",
            value=f"${prediction_dollars:,.0f} CAD"
        )

    with col_range:
        st.metric(
            label="Likely range (±MAE)",
            value=f"${lower_bound:,.0f} — ${upper_bound:,.0f}"
        )

    # Context
    st.markdown(
        f"""
        **What this means:**
        Based on a {property_age}-year-old **{legal_type}** property in
        **{neighbourhood}** zoned as *{zoning}*, the model estimates a market
        value of **${prediction_dollars:,.0f} CAD**.

        The likely range reflects the model's average error (MAE = $376K on the test set).
        """
    )

    # Warning for luxury range
    if prediction_dollars > 5_000_000:
        st.warning(
            "⚠️ This prediction is in the **luxury range ($5M+)**, where the model "
            "tends to underestimate values due to missing features (lot size, square "
            "footage, view). Treat this number as a conservative lower bound.",
            icon="⚠️"
        )

# ============================================================
# Footer
# ============================================================
st.divider()
st.caption(
    "Model: XGBoost regressor trained on 209,000 Vancouver property records (2026). "
    "R² = 0.80 · MAE = $376K · Source: City of Vancouver Open Data Portal."
)