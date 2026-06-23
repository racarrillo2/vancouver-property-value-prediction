# 🏙️ Vancouver Property Value Prediction

Machine learning project that predicts property values in Vancouver, BC using open data from the City of Vancouver. Built as an end-to-end data science portfolio project: from data ingestion via public API to an interactive Streamlit dashboard.

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

- Python (pandas, scikit-learn)
- Jupyter Notebooks
- Streamlit + Folium (interactive map dashboard)
- GitHub

## 📁 Project structure

```
vancouver-property-value-prediction/
├── data/
│   ├── raw/             # Original data from City of Vancouver API
│   └── processed/       # Cleaned data ready for modeling
├── docs/                # Documentation
├── notebooks/
│   ├── 00_data_understanding.ipynb
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   └── 03_modeling.ipynb
├── src/                 # Reusable code modules
├── models/              # Trained models (.pkl)
├── app/                 # Streamlit dashboard
│   ├── Dashboard.py     # Main dashboard page
│   ├── i18n.py          # Internationalization helpers
│   └── translations.py  # Translation strings
├── requirements.txt
└── README.md
```

## 🚀 How to run

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
| **5-fold CV R²** | 0.798 ± 0.003 (stable) |

### Top features by importance

1. **Legal type** (STRATA vs LAND) — 77% importance
2. **Neighbourhood** — 13%
3. **Zoning classification** — 5%
4. **Property age** — 3%
5. **Years since last improvement** — 2%

> The model performs best on mainstream Vancouver properties (1st–99th percentile). It tends to underestimate luxury properties above $5M due to missing physical features (lot size, square footage, view).

## 👤 Author

Rafael Carrillo Mirabal — [LinkedIn](https://www.linkedin.com/in/rafael-carrillo-mirabal/?locale=en) — Vancouver, BC

## 📝 License

MIT