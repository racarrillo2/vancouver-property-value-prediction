"""
Insights page — interactive visualizations of key findings from the EDA.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from i18n import language_selector, tr

# ============================================================
# Page config
# ============================================================
st.set_page_config(page_title="Insights", page_icon="📊", layout="wide")
language_selector()

# ============================================================
# Load data
# ============================================================
@st.cache_data
def load_data():
    data_path = Path(__file__).parent.parent.parent / "data" / "processed" / "property_clean.parquet"
    df = pd.read_parquet(data_path)
    return df

try:
    df = load_data()
except FileNotFoundError:
    st.error("⚠️ Processed data not found.")
    st.stop()

# ============================================================
# Header
# ============================================================
st.title(tr("ins_title"))
st.markdown(tr("ins_subtitle"))
st.divider()

# ============================================================
# Insight 1
# ============================================================
st.header(tr("ins_1_title"))
st.markdown(tr("ins_1_text"))

neighbourhood_stats = (
    df.groupby('neighbourhood_name')['total_value']
    .agg(['median', 'count']).query('count >= 100')
    .sort_values('median', ascending=False).reset_index()
)
neighbourhood_stats['median_millions'] = neighbourhood_stats['median'] / 1e6

fig1 = px.bar(
    neighbourhood_stats,
    x='median_millions', y='neighbourhood_name',
    orientation='h', color='median_millions',
    color_continuous_scale='Blues',
    labels={'median_millions': tr("ins_1_xlabel"), 'neighbourhood_name': tr("ins_1_ylabel")},
    height=600
)
fig1.update_layout(yaxis={'categoryorder': 'total ascending'}, coloraxis_showscale=False, margin=dict(l=0, r=0, t=20, b=0))
st.plotly_chart(fig1, use_container_width=True)

st.divider()

# ============================================================
# Insight 2
# ============================================================
st.header(tr("ins_2_title"))
st.markdown(tr("ins_2_text"))

col1, col2 = st.columns(2)

with col1:
    legal_counts = df['legal_type'].value_counts().reset_index()
    legal_counts.columns = ['legal_type', 'count']
    fig2a = px.pie(legal_counts, values='count', names='legal_type',
                   title=tr("ins_2_count_title"),
                   color_discrete_sequence=px.colors.sequential.Blues_r)
    fig2a.update_layout(margin=dict(l=0, r=0, t=40, b=0))
    st.plotly_chart(fig2a, use_container_width=True)

with col2:
    legal_median = df.groupby('legal_type')['total_value'].median().reset_index()
    legal_median['median_millions'] = legal_median['total_value'] / 1e6
    fig2b = px.bar(legal_median.sort_values('median_millions'),
                   x='median_millions', y='legal_type', orientation='h',
                   title=tr("ins_2_median_title"),
                   labels={'median_millions': tr("ins_2_median_xlabel"), 'legal_type': tr("ins_2_median_ylabel")},
                   color='median_millions', color_continuous_scale='Blues')
    fig2b.update_layout(coloraxis_showscale=False, margin=dict(l=0, r=0, t=40, b=0))
    st.plotly_chart(fig2b, use_container_width=True)

st.divider()

# ============================================================
# Insight 3
# ============================================================
st.header(tr("ins_3_title"))
st.markdown(tr("ins_3_text"))

df_age = df.copy()
df_age['decade_built'] = ((2026 - df_age['property_age']) // 10 * 10).astype(int)
decade_stats = (df_age.groupby('decade_built')['total_value']
                .agg(['median', 'count']).query('count >= 50').reset_index())
decade_stats['median_millions'] = decade_stats['median'] / 1e6
decade_stats = decade_stats[decade_stats['decade_built'] >= 1900]

fig3 = px.bar(decade_stats, x='decade_built', y='median_millions',
              labels={'decade_built': tr("ins_3_xlabel"), 'median_millions': tr("ins_3_ylabel")},
              color='median_millions', color_continuous_scale='Oranges')
fig3.update_layout(coloraxis_showscale=False, margin=dict(l=0, r=0, t=20, b=0))
st.plotly_chart(fig3, use_container_width=True)

st.divider()

# ============================================================
# Insight 4
# ============================================================
st.header(tr("ins_4_title"))
st.markdown(tr("ins_4_text"))

median_val = df['total_value'].median()
fig4 = px.histogram(df, x='total_value', nbins=80,
                    labels={'total_value': tr("ins_4_xlabel")},
                    color_discrete_sequence=['#2E86AB'])
fig4.add_vline(x=median_val, line_dash="dash", line_color="red",
               annotation_text=tr("ins_4_median_annotation", value=median_val),
               annotation_position="top right")
fig4.update_layout(margin=dict(l=0, r=0, t=20, b=0))
st.plotly_chart(fig4, use_container_width=True)

st.divider()
st.subheader(tr("ins_summary_title"))
st.info(tr("ins_summary_text"), icon="💡")