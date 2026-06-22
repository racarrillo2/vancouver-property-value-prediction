"""
Vancouver Property Value Prediction — Streamlit App
Main entry point: project overview and navigation.
"""

import streamlit as st

# ============================================================
# Page configuration (MUST be the first Streamlit command)
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
# Sidebar branding
# ============================================================
with st.sidebar:
    st.title("🏙️ Vancouver Property Predictor")
    st.caption("ML-powered property valuation for the City of Vancouver, BC.")
    st.divider()
    st.markdown("**Navigate** using the menu above ⬆️")
    st.divider()
    st.caption("Built by **Rafael Carrillo Mirabal**")
    st.caption("[GitHub](https://github.com/racarrillo2/vancouver-property-value-prediction) · [LinkedIn](https://www.linkedin.com/in/rafael-carrillo-mirabal/?locale=en)")

# ============================================================
# Main content
# ============================================================
st.title("🏙️ Vancouver Property Value Prediction")
st.markdown(
    "An end-to-end machine learning project that estimates the market value of properties in Vancouver, BC."
)

# Hero metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Model R²", "0.80")
col2.metric("MAE", "$376K")
col3.metric("Training data", "209K properties")
col4.metric("Cross-validation std", "0.003")

st.divider()

# Sections
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("🎯 The problem")
    st.markdown(
        """
        Vancouver has one of the most expensive real estate markets in North America.
        Buyers, investors, and real estate professionals constantly face the question:

        > **Is this property fairly priced?**

        This project answers that with data. Using 209,000 property records from the
        City of Vancouver Open Data Portal, an XGBoost regression model predicts the
        market value of a property based on its location, type, age, and characteristics.
        """
    )

    st.subheader("📊 The data")
    st.markdown(
        """
        - **Source:** [City of Vancouver Open Data Portal](https://opendata.vancouver.ca/explore/dataset/property-tax-report/)
        - **Records:** 1.5M raw → 209K after filtering to 2026 and removing outliers
        - **Features used:** neighbourhood, legal type, zoning, property age, years since improvement
        - **Target:** total property value (land + improvement)
        """
    )

with col_right:
    st.subheader("🛠️ The tech stack")
    st.markdown(
        """
        - **Python** — pandas, scikit-learn, XGBoost
        - **EDA** — Jupyter, matplotlib, seaborn
        - **Modeling** — XGBoost with hyperparameter tuning via RandomizedSearchCV
        - **Validation** — 5-fold cross-validation
        - **Deployment** — Streamlit + Streamlit Cloud
        """
    )

    st.subheader("🚀 What you can do here")
    st.markdown(
        """
        - 🔮 **Predictor** — input property characteristics and get an estimated price
        - 📊 **Insights** — explore the key findings from the data analysis
        - 👤 **About** — learn about the project and the author
        """
    )

st.divider()

st.info(
    "**Disclaimer:** this model is a portfolio project trained on publicly available "
    "data. Predictions are illustrative and should not be used for actual real estate "
    "decisions. The model performs best on mainstream Vancouver properties (1st–99th percentile) "
    "and underestimates luxury properties above $5M due to missing features (lot size, square footage, view).",
    icon="ℹ️"
)