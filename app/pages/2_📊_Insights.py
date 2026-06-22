"""
Insights page — interactive visualizations of key findings from the EDA.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# ============================================================
# Page config
# ============================================================
st.set_page_config(page_title="Insights", page_icon="📊", layout="wide")

# ============================================================
# Load processed data (cached)
# ============================================================
@st.cache_data
def load_data():
    data_path = Path(__file__).parent.parent.parent / "data" / "processed" / "property_clean.parquet"
    df = pd.read_parquet(data_path)
    return df

try:
    df = load_data()
except FileNotFoundError:
    st.error("⚠️ Processed data not found. Run notebook `02_preprocessing.ipynb` first.")
    st.stop()

# ============================================================
# Header
# ============================================================
st.title("📊 Key Insights from the Data")
st.markdown(
    "Findings from analyzing **209,000 Vancouver properties** for the 2026 fiscal year. "
    "These insights drove the modeling decisions."
)
st.divider()

# ============================================================
# Insight 1: Neighbourhood is the #1 price driver
# ============================================================
st.header("1️⃣ Neighbourhood is the #1 price driver")
st.markdown(
    "Property values vary by up to **7x** across Vancouver neighbourhoods. "
    "Location dominates every other factor."
)

neighbourhood_stats = (
    df.groupby('neighbourhood_name')['total_value']
    .agg(['median', 'count'])
    .query('count >= 100')
    .sort_values('median', ascending=False)
    .reset_index()
)
neighbourhood_stats['median_millions'] = neighbourhood_stats['median'] / 1e6

fig1 = px.bar(
    neighbourhood_stats,
    x='median_millions',
    y='neighbourhood_name',
    orientation='h',
    color='median_millions',
    color_continuous_scale='Blues',
    labels={'median_millions': 'Median property value (CAD millions)', 'neighbourhood_name': 'Neighbourhood'},
    height=600
)
fig1.update_layout(
    yaxis={'categoryorder': 'total ascending'},
    coloraxis_showscale=False,
    margin=dict(l=0, r=0, t=20, b=0)
)
st.plotly_chart(fig1, use_container_width=True)

st.divider()

# ============================================================
# Insight 2: STRATA vs LAND — fundamental market split
# ============================================================
st.header("2️⃣ STRATA vs LAND — two different markets")
st.markdown(
    "**STRATA** (condos/apartments) and **LAND** (full ownership) properties have fundamentally different "
    "price structures. The model identifies legal type as its dominant feature (77% importance)."
)

col1, col2 = st.columns(2)

with col1:
    legal_counts = df['legal_type'].value_counts().reset_index()
    legal_counts.columns = ['legal_type', 'count']
    fig2a = px.pie(
        legal_counts,
        values='count',
        names='legal_type',
        title='Property count by legal type',
        color_discrete_sequence=px.colors.sequential.Blues_r
    )
    fig2a.update_layout(margin=dict(l=0, r=0, t=40, b=0))
    st.plotly_chart(fig2a, use_container_width=True)

with col2:
    legal_median = df.groupby('legal_type')['total_value'].median().reset_index()
    legal_median['median_millions'] = legal_median['total_value'] / 1e6
    fig2b = px.bar(
        legal_median.sort_values('median_millions', ascending=True),
        x='median_millions',
        y='legal_type',
        orientation='h',
        title='Median value by legal type',
        labels={'median_millions': 'Median (CAD millions)', 'legal_type': 'Legal type'},
        color='median_millions',
        color_continuous_scale='Blues'
    )
    fig2b.update_layout(coloraxis_showscale=False, margin=dict(l=0, r=0, t=40, b=0))
    st.plotly_chart(fig2b, use_container_width=True)

st.divider()

# ============================================================
# Insight 3: Property age — counterintuitive pattern
# ============================================================
st.header("3️⃣ Older isn't cheaper — it's the opposite")
st.markdown(
    "Properties built **before 1960** are valued ~2x higher than those built after 1970. "
    "This isn't about the buildings — it's about the **land** in established neighbourhoods."
)

df_age = df.copy()
df_age['decade_built'] = ((2026 - df_age['property_age']) // 10 * 10).astype(int)
decade_stats = (
    df_age.groupby('decade_built')['total_value']
    .agg(['median', 'count'])
    .query('count >= 50')
    .reset_index()
)
decade_stats['median_millions'] = decade_stats['median'] / 1e6
decade_stats = decade_stats[decade_stats['decade_built'] >= 1900]

fig3 = px.bar(
    decade_stats,
    x='decade_built',
    y='median_millions',
    labels={'decade_built': 'Decade built', 'median_millions': 'Median value (CAD millions)'},
    color='median_millions',
    color_continuous_scale='Oranges'
)
fig3.update_layout(coloraxis_showscale=False, margin=dict(l=0, r=0, t=20, b=0))
st.plotly_chart(fig3, use_container_width=True)

st.divider()

# ============================================================
# Insight 4: Price distribution is highly skewed
# ============================================================
st.header("4️⃣ The market is heavily right-skewed")
st.markdown(
    "Vancouver's property values follow a long-tail distribution. "
    "Most properties cluster around $1-2M, but a small share extends well into the millions."
)

fig4 = px.histogram(
    df,
    x='total_value',
    nbins=80,
    labels={'total_value': 'Total property value (CAD)'},
    color_discrete_sequence=['#2E86AB']
)
fig4.add_vline(
    x=df['total_value'].median(),
    line_dash="dash",
    line_color="red",
    annotation_text=f"Median: ${df['total_value'].median():,.0f}",
    annotation_position="top right"
)
fig4.update_layout(margin=dict(l=0, r=0, t=20, b=0))
st.plotly_chart(fig4, use_container_width=True)

st.divider()

# ============================================================
# Summary card
# ============================================================
st.subheader("🧠 What this means for the model")
st.info(
    """
    These four insights shaped key modeling decisions:

    - **Log-transformed target** to handle the right-skewed distribution
    - **Tree-based models** (XGBoost, Random Forest) to capture non-linear age patterns
    - **Neighbourhood** as the primary categorical feature
    - **Legal type** as the strongest single predictor (77% feature importance)

    The model achieves **R² = 0.80** on a held-out test set, with **MAE = $376K**.
    """,
    icon="💡"
)