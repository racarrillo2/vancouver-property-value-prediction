"""
About page — project context, author info, and links.
"""

import streamlit as st

st.set_page_config(page_title="About", page_icon="👤", layout="wide")

st.title("👤 About this project")
st.divider()

# ============================================================
# Project section
# ============================================================
st.header("📖 The project")
st.markdown(
    """
    **Vancouver Property Value Prediction** is an end-to-end machine learning portfolio
    project that demonstrates the complete data science workflow:

    1. **Data acquisition** from a real-world open data source
    2. **Exploratory data analysis** to extract business insights
    3. **Preprocessing & feature engineering** with documented decisions
    4. **Model training, tuning, and validation** with multiple algorithms
    5. **Productization** through this interactive Streamlit dashboard
    """
)

# ============================================================
# Author section
# ============================================================
st.divider()
st.header("👋 About the author")

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### Rafael Carrillo Mirabal")
    st.markdown("📍 Vancouver, BC")
    st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/rafael-carrillo-mirabal/?locale=en)")
    st.markdown("[💻 GitHub](https://github.com/racarrillo2)")

with col2:
    st.markdown(
        """
        Aspiring Data Scientist with hands-on experience in the full ML lifecycle: from
        raw data ingestion through model deployment. Currently building a portfolio
        focused on real-world, business-relevant problems.

        **Tech stack:** Python · pandas · scikit-learn · XGBoost · Streamlit · Git · SQL

        **Open to opportunities** in Data Science, Data Analytics, and Machine Learning
        roles in Vancouver and remote-friendly companies.
        """
    )

# ============================================================
# Tech section
# ============================================================
st.divider()
st.header("🛠️ Technical details")

col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Data")
    st.markdown(
        """
        - **Source:** [City of Vancouver Open Data Portal](https://opendata.vancouver.ca/explore/dataset/property-tax-report/)
        - **Raw size:** 1.55M rows × 30 columns
        - **Filtered:** 209K rows × 17 columns (year 2026, 1st–99th percentile)
        - **Format:** Parquet (columnar, type-preserving)
        """
    )

    st.subheader("Model")
    st.markdown(
        """
        - **Algorithm:** XGBoost regressor (gradient boosting)
        - **Target:** `log(total_value)`
        - **Features:** 5 (neighbourhood, legal type, zoning, property age, years since improvement)
        - **Tuning:** RandomizedSearchCV with 20 iterations
        """
    )

with col_b:
    st.subheader("Performance")
    st.markdown(
        """
        - **R²:** 0.80
        - **MAE:** $376,432 CAD
        - **RMSE:** $857,255 CAD
        - **5-fold CV:** R² = 0.798 ± 0.003 (stable)
        """
    )

    st.subheader("Limitations")
    st.markdown(
        """
        - Designed for mainstream properties (1st–99th percentile)
        - Underestimates luxury properties ($5M+) due to missing physical features
        - Future v2: integrate lot size, square footage, and proximity features
        """
    )

# ============================================================
# Links
# ============================================================
st.divider()
st.header("🔗 Links")

col_x, col_y, col_z = st.columns(3)

with col_x:
    st.link_button(
        "💻 View source code",
        "https://github.com/racarrillo2/vancouver-property-value-prediction",
        use_container_width=True
    )

with col_y:
    st.link_button(
        "🔗 Connect on LinkedIn",
        "https://www.linkedin.com/in/rafael-carrillo-mirabal/?locale=en",
        use_container_width=True
    )

with col_z:
    st.link_button(
        "📊 Data source",
        "https://opendata.vancouver.ca/explore/dataset/property-tax-report/",
        use_container_width=True
    )

# ============================================================
# Footer
# ============================================================
st.divider()
st.caption(
    "Built with Python, scikit-learn, XGBoost, and Streamlit. "
    "Source code and full documentation available on GitHub."
)