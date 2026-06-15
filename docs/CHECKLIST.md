# 📋 Project Checklist — Vancouver Property Value Prediction

> End-to-end roadmap for the data science portfolio project. Tracks progress from data acquisition to final presentation.

---

## 🟢 Phase 0 — Setup ✅

- [x] Define main project idea and plan B
- [x] Find and validate datasets (main + backup)
- [x] Create GitHub repository with professional structure
- [x] Initial README in English
- [x] `.gitignore` and `requirements.txt` configured
- [x] LinkedIn linked in README

---

## 🟡 Phase 1 — Data Acquisition & Initial Exploration

**Goal:** understand what we have before touching anything.

- [ ] Download CSV from Vancouver Property Tax Report portal
- [ ] Save it as `data/raw/property_tax_report.csv`
- [ ] Check file size and number of rows/columns
- [ ] Create notebook `notebooks/00_data_understanding.ipynb`:
  - [ ] Load CSV with pandas (likely `sep=";"`)
  - [ ] `df.shape`, `df.dtypes`, `df.info()`, `df.describe()`
  - [ ] Identify target variable (`current_land_value` + `current_improvement_value`)
  - [ ] Identify candidate features (zoning, year built, neighbourhood, etc.)
  - [ ] Document first observations in Markdown cells

**Deliverable:** notebook with commented first look at the dataset.

---

## 🟡 Phase 2 — Exploratory Data Analysis (EDA)

**Goal:** understand the story the data tells. This is what impresses recruiters the most.

📓 Notebook: `notebooks/01_eda.ipynb`

### 2.1 Univariate analysis
- [ ] Price distribution (histogram + boxplot) — likely skewed
- [ ] Outlier analysis ($10M+ properties, industrial lots, etc.)
- [ ] Distribution of `year_built`, `tax_levy`, `zoning_classification`
- [ ] Property count per neighbourhood (`neighbourhood_code`)

### 2.2 Bivariate analysis
- [ ] Price vs. year built
- [ ] Price vs. property type (`legal_type`: strata, land...)
- [ ] Price vs. zoning
- [ ] Price vs. neighbourhood (top 10 most expensive / cheapest)
- [ ] Price evolution over the years (`report_year` / `tax_assessment_year`)

### 2.3 Multivariate analysis
- [ ] Correlation matrix between numeric variables
- [ ] Seaborn heatmap

### 2.4 EDA conclusions
- [ ] Markdown cell with **5–7 key insights** (these go straight into the final presentation)

**Deliverable:** notebook with clean charts and written findings.

---

## 🟡 Phase 3 — Preprocessing & Cleaning

**Goal:** prepare the dataset for training.

📓 Notebook: `notebooks/02_preprocessing.ipynb`

### 3.1 Cleaning
- [ ] Handle null values (per-column strategy)
- [ ] Drop useless columns (IDs, long legal descriptions)
- [ ] Handle outliers (winsorization or removal as appropriate)
- [ ] Convert data types (dates, categoricals)

### 3.2 Feature engineering (the creative part that differentiates the project)
- [ ] `property_age` = current year − `year_built`
- [ ] `total_value` = `current_land_value` + `current_improvement_value`
- [ ] `land_to_total_ratio` = `current_land_value` / `total_value`
- [ ] `years_since_improvement` = current year − `big_improvement_year`
- [ ] One-hot encoding for `zoning_classification`, `neighbourhood_code`, `legal_type`
- [ ] (Optional advanced) Cross with **parks** and **schools** datasets from the same portal to compute distance to nearest park/school — this elevates the project from good to outstanding

### 3.3 Final datasets
- [ ] `X` / `y` split
- [ ] `train_test_split` (80/20, `random_state=42`)
- [ ] Scale with `StandardScaler` for linear models
- [ ] Save processed dataset to `data/processed/property_clean.csv`

**Deliverable:** notebook + processed CSV ready for modeling.

---

## 🟡 Phase 4 — Modeling & Evaluation

**Goal:** train multiple models, compare, pick the best.

📓 Notebook: `notebooks/03_modeling.ipynb`

### 4.1 Models to train (in this order)
- [ ] **Baseline:** always predict the mean (starting point)
- [ ] Linear Regression
- [ ] Random Forest Regressor
- [ ] XGBoost / LightGBM (industry standards)
- [ ] (Optional) Gradient Boosting Regressor

### 4.2 Evaluation
- [ ] Metrics: **MAE, RMSE, R²** (all three in a comparison table)
- [ ] 5-fold cross-validation for robustness
- [ ] Predicted vs. actual plot
- [ ] Residuals plot
- [ ] **Feature importance** of the best model (key for interview explanations)

### 4.3 Hyperparameter tuning
- [ ] GridSearchCV or RandomizedSearchCV on the best model
- [ ] Save final model to `models/best_model.pkl` with `joblib`

**Deliverable:** notebook + trained model + metrics comparison table.

---

## 🟡 Phase 5 — Product: Streamlit Dashboard

**Goal:** anyone can use the model without knowing Python.

📁 Folder: `app/`

- [ ] `app/app.py` with the main application
- [ ] **Page 1: Home** — project explanation, problem solved, Vancouver context
- [ ] **Page 2: Data explorer** — neighbourhood filters, interactive Folium map
- [ ] **Page 3: Predictor** — form for inputs + price estimation with confidence interval
- [ ] **Page 4: Insights** — key EDA charts
- [ ] Clean design (sidebar navigation, consistent colors)
- [ ] Test locally with `streamlit run app/app.py`
- [ ] **Deploy free on Streamlit Cloud** → gives you a public link for your CV/LinkedIn

**Deliverable:** working app + public link.

---

## 🟡 Phase 6 — Final Documentation

**Goal:** repo ready to be seen by recruiters.

- [ ] Update README with:
  - [ ] App screenshots
  - [ ] Results/metrics table
  - [ ] Demo GIF or link to deployed app
  - [ ] "Key insights" section
- [ ] Create `docs/PRESENTATION.md` with business-focused project summary
- [ ] Clean notebooks (run top-to-bottom without errors)
- [ ] Update `requirements.txt` with specific versions (`pip freeze > requirements.txt`)
- [ ] Verify anyone can clone and run the project following the README

**Deliverable:** polished public repo ready to show.

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