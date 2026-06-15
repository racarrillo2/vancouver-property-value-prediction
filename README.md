# 🏙️ Vancouver Property Value Prediction

Machine learning project that predicts property values in Vancouver, BC using open data from the City of Vancouver. Built as an end-to-end data science portfolio project: from data ingestion via public API to an interactive Streamlit dashboard.

## 🎯 Problem statement

Vancouver has one of the most expensive real estate markets in North America. This project helps buyers, investors, and real estate professionals estimate whether a property is fairly priced based on its characteristics, location, and neighbourhood.

## 📊 Data source

- **City of Vancouver Open Data Portal** — Property Tax Report
  https://opendata.vancouver.ca/explore/dataset/property-tax-report/

## 🛠️ Tech stack

- Python (pandas, scikit-learn)
- Jupyter Notebooks
- Streamlit + Folium (interactive map dashboard)
- GitHub

## 📁 Project structure

\```
vancouver-property-value-prediction/
├── data/
│   ├── raw/             # Original data from City of Vancouver API
│   └── processed/       # Cleaned data ready for modeling
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   └── 03_modeling.ipynb
├── src/                 # Reusable code modules
├── models/              # Trained models (.pkl)
├── app/                 # Streamlit dashboard
├── requirements.txt
└── README.md
\```

## 🚀 How to run

\```bash
git clone https://github.com/racarrillo2/vancouver-property-value-prediction.git
cd vancouver-property-value-prediction
pip install -r requirements.txt
streamlit run app/app.py
\```

## 📈 Results

*Coming soon — model metrics, feature importance, and dashboard screenshots.*

## 👤 Author

Rafael Carrillo Mirabal — https://www.linkedin.com/in/rafael-carrillo-mirabal/?locale=en — Vancouver, BC

## 📝 License

MIT