# 🏙️ Vancouver Property Value Prediction

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://vancouver-property-value-prediction.streamlit.app)

Machine learning project that predicts property values in Vancouver, BC using open data from the City of Vancouver. Built as an end-to-end data science portfolio project: from open data download to an interactive Streamlit dashboard.

> 🌐 **Available in English and Spanish** — use the language selector in the sidebar.

## 🎯 Problem statement

Vancouver has one of the most expensive real estate markets in North America. This project helps buyers, investors, and real estate professionals estimate whether a property is fairly priced based on its characteristics, location, and neighbourhood.

## 📊 Data source

Property Tax Report from the City of Vancouver Open Data Portal.

**Download instructions:**
1. Go to https://opendata.vancouver.ca/explore/dataset/property-tax-report/
2. Click on "Export" → download as Parquet
3. Save the file as `data/raw/property_tax_report.parquet`

The dataset is not included in this repository due to file size limits.

## 🛠️ Tech stack

- **Python** — pandas, numpy, scikit-learn, XGBoost
- **EDA** — Jupyter, matplotlib, seaborn
- **App** — Streamlit + Plotly (interactive dashboard)
- **Deployment** — Streamlit Community Cloud
- **i18n** — bilingual support (EN/ES)
- **Version control** — Git + GitHub

## 📁 Project structure

```
vancouver-property-value-prediction/
├── .devcontainer/       # Dev container configuration
├── .streamlit/          # Streamlit Cloud config (theme, headless)
├── app/                 # Streamlit dashboard
│   ├── Dashboard.py     # Main entry point (home page)
│   ├── language_utils.py  # Language selector & i18n helpers
│   ├── translations.py  # Translation strings (EN/ES)
│   └── pages/           # Multi-page app pages
│       ├── 1_🔮_Predictor.py    # Property value predictor
│       ├── 2_📊_Insights.py     # EDA insights & charts
│       └── 3_👤_About.py        # Project info & author
├── data/
│   ├── raw/             # Original data from City of Vancouver Open Data Portal
│   └── processed/       # Cleaned data ready for modeling
├── docs/                # Documentation & presentation deck
│   ├── CHECKLIST.md
│   └── PRESENTATION.md
├── models/              # Trained models (.pkl, .joblib)
│   ├── best_model.pkl
│   ├── model_metadata.pkl
│   └── permutation_importance.json
├── notebooks/           # Jupyter notebooks (phases 0–3)
│   ├── 00_data_understanding.ipynb
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   └── 03_modeling.ipynb
├── src/                 # Reusable Python package
│   ├── __init__.py
│   ├── config.py        # App constants (paths, year, MAE)
│   ├── data_utils.py    # Data loading utilities
│   └── model_utils.py   # Model loading utilities
├── .gitignore
├── LICENSE
├── requirements.txt
└── README.md
```

## 🚀 How to run

### 🌐 Live app

[https://vancouver-property-value-prediction.streamlit.app](https://vancouver-property-value-prediction.streamlit.app)

### 🖥️ Run locally

```bash
git clone https://github.com/racarrillo2/vancouver-property-value-prediction.git
cd vancouver-property-value-prediction
pip install -r requirements.txt
streamlit run app/Dashboard.py
```

## 📈 Results

**Final model:** XGBoost regressor (hyperparameter-tuned via RandomizedSearchCV)

| Metric | Value |
|---|---|
| **R²** (test set) | **0.80** |
| **MAE** (test set) | **$376,432 CAD** |
| **RMSE** (test set) | **$857,255 CAD** |
| **MAPE** (test set) | **15.6%** (median percentage error) |
| **5-fold CV R²** | 0.798 ± 0.003 (stable) |
| **Training data** | 209,000 properties |

### Top features by importance

*Using permutation importance (scikit-learn), which is more reliable than XGBoost's built-in importance for datasets with categorical features. Values show the drop in R² when each feature is randomly shuffled — higher = more important.*

| Feature | R² drop | Normalized importance |
|---------|--------:|---------------------:|
| **Legal type** (STRATA vs LAND) | 1.273 | **50.0%** |
| **Neighbourhood** | 0.500 | **19.6%** |
| **Years since improvement** | 0.294 | 11.5% |
| **Zoning classification** | 0.281 | 11.0% |
| **Property age** | 0.201 | 7.9% |

**Legal type is ~2.55× more important than neighbourhood**, confirming that Vancouver's market is primarily segmented by property type (condo vs land), with location as the strong secondary driver.

### Key insights from the data

- 📍 **Location drives massive price variance** — property values vary by up to **7x** across Vancouver neighbourhoods (Shaughnessy $4.4M median vs East Hastings $0.65M median), but **legal type (STRATA vs LAND)** is the model's single strongest predictor (~2.55× more important than neighbourhood)
- 🏘️ **STRATA vs LAND** are fundamentally different markets — captured as the strongest single feature
- 🏛️ **Older isn't cheaper** — pre-1960 properties are valued ~2x higher than 1970–2000 builds (land value in established neighbourhoods)
- 📊 The market is **heavily right-skewed**, justifying log-transformation of the target

> The model was trained on mainstream Vancouver properties (1st–99th percentile, excluding the top 1% of extreme values). This limits accuracy on luxury properties above ~$5M. Future iterations would integrate BC Assessment property dimensions and amenity proximity features.

## 👤 Author

Rafael Carrillo Mirabal — [LinkedIn](https://www.linkedin.com/in/rafael-carrillo-mirabal/?locale=en) — Vancouver, BC

## 📝 License

MIT