# 📋 Project Checklist — Vancouver Property Value Prediction

> End-to-end roadmap for the data science portfolio project. Tracks progress from data acquisition to final presentation.

**Last updated:** Phase 5 (Dashboard partial) — checklist synced with actual progress

---

## 🟢 Phase 0 — Setup ✅ COMPLETE

- [x] Define main project idea and plan B
- [x] Find and validate datasets (main + backup)
- [x] Create GitHub repository with professional structure
- [x] Initial README in English
- [x] `.gitignore` and `requirements.txt` configured
- [x] LinkedIn linked in README

---

## 🟢 Phase 1 — Data Acquisition & Initial Exploration ✅ COMPLETE

**Goal:** understand what we have before touching anything.

- [x] Download dataset from Vancouver Property Tax Report portal (**Parquet format**)
- [x] Save it as `data/raw/property_tax_report.parquet`
- [x] Check file size (134 MB on disk, 691 MB in RAM) and dimensions (1.55M rows × 30 columns)
- [x] Create notebook `notebooks/00_data_understanding.ipynb`:
  - [x] Load Parquet with pandas + pyarrow
  - [x] `df.shape`, `df.dtypes`, `df.info()`, `df.describe()`
  - [x] Compare numeric vs categorical describe (`include='object'`)
  - [x] Identify target variable (`current_land_value` + `current_improvement_value`)
  - [x] Identify candidate features (neighbourhood, zoning, legal_type, year_built)
  - [x] Detect year columns stored as strings (need conversion later)
  - [x] Detect high-null columns (`note`, `narrative_legal_line3-5`)
  - [x] Document first observations in Markdown cells

**Deliverable:** ✅ notebook with commented first look at the dataset.

---

## 🟢 Phase 2 — Exploratory Data Analysis (EDA) ✅ COMPLETE

**Goal:** understand the story the data tells.

📓 Notebook: `notebooks/01_eda.ipynb`

### 2.1 Univariate analysis
- [x] Price distribution — linear, log, and boxplot
- [x] Outlier analysis (filtered to 1st–99th percentile for clean visualization)
- [x] Distribution per `report_year`

### 2.2 Bivariate analysis
- [x] Price vs. `year_built` (decade analysis — discovered "step pattern" pre/post 1970)
- [x] Price vs. `legal_type` (STRATA vs LAND vs others)
- [x] Price vs. `neighbourhood_code` (top 10 / bottom 10 — discovered 7x price ratio)
- [x] Land vs. improvement ratio analysis
- [x] Temporal evolution 2020–2026

### 2.3 Multivariate analysis
- [x] Correlation matrix between numeric variables
- [x] Seaborn heatmap

### 2.4 EDA conclusions
- [x] **7 key insights documented** for final presentation:
  1. Right-skewed target → log-transform
  2. STRATA vs LAND have different price structures
  3. Neighbourhood = #1 price driver (7x ratio)
  4. Property age has step-pattern (pre/post 1970)
  5. Vancouver market is land-driven
  6. Significant price evolution 2020–2026
  7. ⚠️ Data leakage detected in `tax_levy` and `previous_*` columns

**Deliverable:** ✅ notebook with 7 actionable insights.

---

## 🟢 Phase 3 — Preprocessing & Cleaning ✅ COMPLETE

**Goal:** prepare the dataset for training.

📓 Notebook: `notebooks/02_preprocessing.ipynb`

### 3.1 Data enrichment
- [x] **Cross with "Local area boundary" dataset** to map `neighbourhood_code` → real neighbourhood names (Shaughnessy, Kerrisdale, etc.)
- [x] Validate the mapping coverage

### 3.2 Cleaning
- [x] Convert year columns to numeric: `year_built`, `report_year`, `big_improvement_year`, `tax_assessment_year`
- [x] Drop useless columns: `note`, `narrative_legal_line3-5`, long legal descriptions
- [x] **Exclude data leakage columns:** `tax_levy`, `previous_land_value`, `previous_improvement_value`
- [x] Handle null values (per-column strategy)
- [x] Handle outliers (filter or winsorize)
- [x] Filter to most recent year (2026) for the main model

### 3.3 Feature engineering
- [x] `property_age` = 2026 − `year_built`
- [x] `total_value` = `current_land_value` + `current_improvement_value`
- [x] `land_to_total_ratio` = `current_land_value` / `total_value`
- [x] `years_since_improvement` = 2026 − `big_improvement_year`
- [x] `log_total_value` (target for modeling)
- [x] Encoding for categorical features (target encoding for neighbourhood, one-hot for legal_type/zoning)
- [ ] (Optional advanced) Cross with **parks/schools** datasets for proximity features

### 3.4 Final datasets
- [x] `X` / `y` split
- [x] `train_test_split` (80/20, `random_state=42`)
- [x] Scale with `StandardScaler` for linear models
- [x] Save processed dataset to `data/processed/property_clean.parquet`

**Deliverable:** ✅ notebook + processed dataset ready for modeling.

---

## 🟢 Phase 4 — Modeling & Evaluation ✅ COMPLETE

**Goal:** train multiple models, compare, pick the best.

📓 Notebook: `notebooks/03_modeling.ipynb`

### 4.1 Models to train (in this order)
- [x] **Baseline:** always predict the mean (sanity check)
- [x] Linear Regression
- [x] Random Forest Regressor
- [x] XGBoost (industry standard, chosen as final model)
- [ ] (Optional) Gradient Boosting Regressor

### 4.2 Evaluation
- [x] Metrics: **MAE, RMSE, R²** (all three in a comparison table)
- [x] 5-fold cross-validation for robustness
- [x] Predicted vs. actual plot
- [x] Residuals plot
- [x] **Feature importance** of the best model
- [ ] SHAP values (optional, very impressive for interviews)

### 4.3 Hyperparameter tuning
- [x] RandomizedSearchCV on XGBoost
- [x] Save final model to `models/best_model.pkl` with `joblib`

**Deliverable:** ✅ notebook + trained model + metrics comparison table.

---

## 🟡 Phase 5 — Product: Streamlit Dashboard (partial)

**Goal:** anyone can use the model without knowing Python.

📁 Folder: `app/`

- [x] `app/Dashboard.py` with the main application
- [x] **Page 1: Home** — project explanation, Vancouver context
- [x] **Page 2: Map** — interactive Folium choropleth of property values by neighbourhood
- [x] **Page 3: Predictor** — input form + price estimation
- [x] **Page 4: Insights** — key EDA charts
- [x] **Page 5: About** — project info and author
- [x] Clean design (sidebar navigation, consistent colors, bilingual EN/ES)
- [x] Test locally with `streamlit run app/Dashboard.py`
- [x] **Deploy free on Streamlit Cloud** → [vancouver-property-value-prediction.streamlit.app](https://vancouver-property-value-prediction.streamlit.app)

**Deliverable:** working app deployed at [vancouver-property-value-prediction.streamlit.app](https://vancouver-property-value-prediction.streamlit.app).

---

## 🟡 Phase 6 — Final Documentation (partial)

**Goal:** repo ready to be seen by recruiters.

- [x] Update README with:
  - [ ] App screenshots
  - [x] Results/metrics table
  - [x] Link to deployed app: [vancouver-property-value-prediction.streamlit.app](https://vancouver-property-value-prediction.streamlit.app)
  - [ ] "Key insights" section
- [ ] Create `docs/PRESENTATION.md` with business-focused summary
- [x] Clean notebooks (run top-to-bottom without errors)
- [x] Update `requirements.txt` with specific versions
- [x] Add data download instructions in README
- [x] Verify anyone can clone and run the project
- [x] Refactored shared code into `src/` reusable modules

**Deliverable:** mostly polished — missing screenshots and Presentation.md. Deployed at [vancouver-property-value-prediction.streamlit.app](https://vancouver-property-value-prediction.streamlit.app).

---

## 🟡 Phase 7 — Final Presentation

**Goal:** sell the project to companies, not explain the code.

- [ ] Slides in PowerPoint / Google Slides (10–12 slides max)
- [ ] Suggested structure:
  1. Problem and context (Vancouver housing crisis)
  2. Data (source, volume, quality)
  3. EDA — top 3 visual insights
  4. Chosen model and why
  5. Metrics and validation
  6. Live Streamlit demo
  7. Limitations and next steps
  8. Question to open audience conversation
- [ ] **Rehearse out loud** at least 3 times
- [ ] Prepare answers to: "Why this model?", "What would you do differently with more time?", "How would you put it in production?"

**Deliverable:** presentation ready + you ready to defend it.

---

## 🎯 Key Milestones

| Milestone | When | Status |
|---|---|---|
| **Milestone 1** | End of Phase 2 | ✅ **DONE** — Vancouver story told with 7 insights |
| **Milestone 2** | End of Phase 4 | ✅ **DONE** — XGBoost with R² = 0.80 |
| **Milestone 3** | End of Phase 5 | ✅ **DONE** — [vancouver-property-value-prediction.streamlit.app](https://vancouver-property-value-prediction.streamlit.app) |
| **Milestone 4** | End of Phase 7 | ⬜ Pending — 5-min pitch ready |

---

## 💡 Pro Tips

1. **Commit often.** Every meaningful step → commit + push.
2. **Professional commit messages:** `feat: ...`, `fix: ...`, `docs: ...`.
3. **Speak with data, not opinions.**
4. **Iterate, don't perfect.** Better all phases at 70% than Phase 1 at 100%.

---

## 📊 Key findings carried into next phases

- ⚠️ **Exclude from features (data leakage):** `tax_levy`, `previous_land_value`, `previous_improvement_value`
- 🔄 **Type conversions needed:** all year columns are strings
- 🧹 **Drop columns:** `note`, `narrative_legal_line3-5`, `block`, `from_civic_number`
- 🎯 **Strong features confirmed:** `neighbourhood_code`, `legal_type`, `zoning_classification`, `year_built`
- 📉 **Target transformation:** use `log(total_value)`
- 🗺️ **Enrichment needed:** map neighbourhood codes to real names