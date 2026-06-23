"""
Translations dictionary for the Vancouver Property Predictor app.
Supports English (en) and Spanish (es).
"""

TRANSLATIONS = {
    # ============================================================
    # COMMON
    # ============================================================
    "language_label": {"en": "🌐 Language", "es": "🌐 Idioma"},
    "sidebar_title": {"en": "🏙️ Vancouver Property Predictor", "es": "🏙️ Predictor de Propiedades Vancouver"},
    "sidebar_caption": {
        "en": "ML-powered property valuation for the City of Vancouver, BC.",
        "es": "Valoración de propiedades con ML para la Ciudad de Vancouver, BC."
    },
    "sidebar_navigate": {"en": "**Navigate** using the menu above ⬆️", "es": "**Navega** usando el menú de arriba ⬆️"},
    "sidebar_built_by": {"en": "Built by **Rafael Carrillo Mirabal**", "es": "Hecho por **Rafael Carrillo Mirabal**"},

    # ============================================================
    # HOME PAGE
    # ============================================================
    "home_title": {"en": "🏙️ Vancouver Property Value Prediction", "es": "🏙️ Predicción del Valor de Propiedades en Vancouver"},
    "home_subtitle": {
        "en": "An end-to-end machine learning project that estimates the market value of properties in Vancouver, BC.",
        "es": "Un proyecto de machine learning de principio a fin que estima el valor de mercado de propiedades en Vancouver, BC."
    },
    "metric_r2": {"en": "Model R²", "es": "R² del modelo"},
    "metric_mae": {"en": "MAE", "es": "MAE"},
    "metric_training": {"en": "Training data", "es": "Datos de entrenamiento"},
    "metric_training_value": {"en": "209K properties", "es": "209K propiedades"},
    "metric_cv": {"en": "Cross-validation std", "es": "Desv. estándar CV"},
    "home_problem_title": {"en": "🎯 The problem", "es": "🎯 El problema"},
    "home_problem_text": {
        "en": (
            "Vancouver has one of the most expensive real estate markets in North America. "
            "Buyers, investors, and real estate professionals constantly face the question:\n\n"
            "> **Is this property fairly priced?**\n\n"
            "This project answers that with data. Using 209,000 property records from the "
            "City of Vancouver Open Data Portal, an XGBoost regression model predicts the "
            "market value of a property based on its location, type, age, and characteristics."
        ),
        "es": (
            "Vancouver tiene uno de los mercados inmobiliarios más caros de Norteamérica. "
            "Compradores, inversores y profesionales del sector se enfrentan constantemente a la pregunta:\n\n"
            "> **¿El precio de esta propiedad es justo?**\n\n"
            "Este proyecto responde con datos. Usando 209.000 registros de propiedades del "
            "Portal de Datos Abiertos de la Ciudad de Vancouver, un modelo de regresión XGBoost "
            "predice el valor de mercado de una propiedad según su ubicación, tipo, edad y características."
        )
    },
    "home_data_title": {"en": "📊 The data", "es": "📊 Los datos"},
    "home_data_text": {
        "en": (
            "- **Source:** [City of Vancouver Open Data Portal](https://opendata.vancouver.ca/explore/dataset/property-tax-report/)\n"
            "- **Records:** 1.5M raw → 209K after filtering to 2026 and removing outliers\n"
            "- **Features used:** neighbourhood, legal type, zoning, property age, years since improvement\n"
            "- **Target:** total property value (land + improvement)"
        ),
        "es": (
            "- **Fuente:** [Portal de Datos Abiertos de Vancouver](https://opendata.vancouver.ca/explore/dataset/property-tax-report/)\n"
            "- **Registros:** 1,5M brutos → 209K tras filtrar a 2026 y eliminar outliers\n"
            "- **Variables usadas:** barrio, tipo legal, zonificación, antigüedad, años desde renovación\n"
            "- **Objetivo:** valor total de la propiedad (terreno + edificación)"
        )
    },
    "home_tech_title": {"en": "🛠️ The tech stack", "es": "🛠️ Stack tecnológico"},
    "home_tech_text": {
        "en": (
            "- **Python** — pandas, scikit-learn, XGBoost\n"
            "- **EDA** — Jupyter, matplotlib, seaborn\n"
            "- **Modeling** — XGBoost with hyperparameter tuning via RandomizedSearchCV\n"
            "- **Validation** — 5-fold cross-validation\n"
            "- **Deployment** — Streamlit + Streamlit Cloud"
        ),
        "es": (
            "- **Python** — pandas, scikit-learn, XGBoost\n"
            "- **EDA** — Jupyter, matplotlib, seaborn\n"
            "- **Modelado** — XGBoost con ajuste de hiperparámetros vía RandomizedSearchCV\n"
            "- **Validación** — Cross-validation de 5 folds\n"
            "- **Despliegue** — Streamlit + Streamlit Cloud"
        )
    },
    "home_what_title": {"en": "🚀 What you can do here", "es": "🚀 Qué puedes hacer aquí"},
    "home_what_text": {
        "en": (
            "- 🗺️ **Map** — explore property values across Vancouver neighbourhoods\n"
            "- 🔮 **Predictor** — input property characteristics and get an estimated price\n"
            "- 📊 **Insights** — explore the key findings from the data analysis\n"
            "- 👤 **About** — learn about the project and the author"
        ),
        "es": (
            "- 🗺️ **Mapa** — explora los valores de propiedades por barrio\n"
            "- 🔮 **Predictor** — introduce características y obtén un precio estimado\n"
            "- 📊 **Insights** — explora los hallazgos clave del análisis\n"
            "- 👤 **Acerca de** — conoce el proyecto y al autor"
        )
    },
    "home_disclaimer": {
        "en": (
            "**Disclaimer:** this model is a portfolio project trained on publicly available "
            "data. Predictions are illustrative and should not be used for actual real estate "
            "decisions. The model performs best on mainstream Vancouver properties (1st–99th percentile) "
            "and underestimates luxury properties above $5M due to missing features (lot size, square footage, view)."
        ),
        "es": (
            "**Aviso:** este modelo es un proyecto de portafolio entrenado con datos públicos. "
            "Las predicciones son ilustrativas y no deben usarse para decisiones inmobiliarias reales. "
            "El modelo funciona mejor con propiedades típicas de Vancouver (percentil 1-99) y "
            "subestima propiedades de lujo por encima de los $5M por falta de features físicas (tamaño del lote, m², vistas)."
        )
    },

    # ============================================================
    # PREDICTOR PAGE
    # ============================================================
    "pred_title": {"en": "🔮 Property Value Predictor", "es": "🔮 Predictor de Valor de Propiedad"},
    "pred_subtitle": {
        "en": "Enter the characteristics of a Vancouver property to get an estimated market value.",
        "es": "Introduce las características de una propiedad en Vancouver para obtener un valor estimado."
    },
    "pred_location_section": {"en": "📍 Location & type", "es": "📍 Ubicación y tipo"},
    "pred_neighbourhood": {"en": "Neighbourhood", "es": "Barrio"},
    "pred_neighbourhood_help": {"en": "The Vancouver neighbourhood where the property is located.", "es": "El barrio de Vancouver donde se ubica la propiedad."},
    "pred_legal_type": {"en": "Legal type", "es": "Tipo legal"},
    "pred_legal_type_help": {"en": "STRATA = condo/apartment unit. LAND = full land ownership (house, lot).", "es": "STRATA = condominio/apartamento. LAND = propiedad completa del terreno (casa, parcela)."},
    "pred_zoning": {"en": "Zoning classification", "es": "Clasificación urbanística"},
    "pred_zoning_help": {"en": "The zoning category assigned by the City of Vancouver.", "es": "Categoría urbanística asignada por la Ciudad de Vancouver."},
    "pred_characteristics_section": {"en": "🏗️ Property characteristics", "es": "🏗️ Características de la propiedad"},
    "pred_year_built": {"en": "Year built", "es": "Año de construcción"},
    "pred_year_built_help": {"en": "The year the property was originally constructed.", "es": "Año en que se construyó originalmente la propiedad."},
    "pred_year_improved": {"en": "Year of last major improvement (renovation)", "es": "Año de la última renovación importante"},
    "pred_year_improved_help": {"en": "The year of the most recent significant renovation. If never renovated, set equal to year built.", "es": "Año de la última renovación significativa. Si nunca se renovó, ponlo igual al año de construcción."},
    "pred_age_info": {"en": "**Property age:** {years} years", "es": "**Antigüedad:** {years} años"},
    "pred_improvement_info": {"en": "**Years since last improvement:** {years} years", "es": "**Años desde última renovación:** {years} años"},
    "pred_button": {"en": "🔮 Predict property value", "es": "🔮 Predecir valor"},
    "pred_result_title": {"en": "💰 Estimated value", "es": "💰 Valor estimado"},
    "pred_predicted_label": {"en": "Predicted property value", "es": "Valor estimado de la propiedad"},
    "pred_range_label": {"en": "Likely range (±MAE)", "es": "Rango probable (±MAE)"},
    "pred_explanation": {
        "en": "**What this means:**\nBased on a {age}-year-old **{legal_type}** property in **{neighbourhood}** zoned as *{zoning}*, the model estimates a market value of **${value:,.0f} CAD**.\n\nThe likely range reflects the model's average error (MAE = $376K on the test set).",
        "es": "**Qué significa esto:**\nPara una propiedad **{legal_type}** de {age} años en **{neighbourhood}** con zonificación *{zoning}*, el modelo estima un valor de mercado de **${value:,.0f} CAD**.\n\nEl rango probable refleja el error medio del modelo (MAE = $376K en el conjunto de prueba)."
    },
    "pred_luxury_warning": {
        "en": "⚠️ This prediction is in the **luxury range ($5M+)**, where the model tends to underestimate values due to missing features (lot size, square footage, view). Treat this number as a conservative lower bound.",
        "es": "⚠️ Esta predicción está en el **rango de lujo ($5M+)**, donde el modelo tiende a subestimar valores por falta de features (tamaño del lote, m², vistas). Considera este número como una cota inferior conservadora."
    },
    "pred_footer": {
        "en": "Model: XGBoost regressor trained on 209,000 Vancouver property records (2026). R² = 0.80 · MAE = $376K · Source: City of Vancouver Open Data Portal.",
        "es": "Modelo: regresor XGBoost entrenado con 209.000 registros de propiedades de Vancouver (2026). R² = 0,80 · MAE = $376K · Fuente: Portal de Datos Abiertos de Vancouver."
    },

    # ============================================================
    # INSIGHTS PAGE
    # ============================================================
    "ins_title": {"en": "📊 Key Insights from the Data", "es": "📊 Hallazgos Clave del Análisis"},
    "ins_subtitle": {
        "en": "Findings from analyzing **209,000 Vancouver properties** for the 2026 fiscal year. These insights drove the modeling decisions.",
        "es": "Resultados del análisis de **209.000 propiedades en Vancouver** para el año fiscal 2026. Estos hallazgos guiaron las decisiones del modelo."
    },
    "ins_1_title": {"en": "1️⃣ Neighbourhood is the #1 price driver", "es": "1️⃣ El barrio es el factor #1 del precio"},
    "ins_1_text": {
        "en": "Property values vary by up to **7x** across Vancouver neighbourhoods. Location dominates every other factor.",
        "es": "Los valores de propiedad varían hasta **7x** entre barrios de Vancouver. La ubicación domina cualquier otro factor."
    },
    "ins_1_xlabel": {"en": "Median property value (CAD millions)", "es": "Valor mediano (millones CAD)"},
    "ins_1_ylabel": {"en": "Neighbourhood", "es": "Barrio"},
    "ins_2_title": {"en": "2️⃣ STRATA vs LAND — two different markets", "es": "2️⃣ STRATA vs LAND — dos mercados distintos"},
    "ins_2_text": {
        "en": "**STRATA** (condos/apartments) and **LAND** (full ownership) properties have fundamentally different price structures. The model identifies legal type as its dominant feature (77% importance).",
        "es": "Las propiedades **STRATA** (condominios/apartamentos) y **LAND** (propiedad completa) tienen estructuras de precio fundamentalmente distintas. El modelo identifica el tipo legal como su feature dominante (77% de importancia)."
    },
    "ins_2_count_title": {"en": "Property count by legal type", "es": "Cantidad de propiedades por tipo legal"},
    "ins_2_median_title": {"en": "Median value by legal type", "es": "Valor mediano por tipo legal"},
    "ins_2_median_xlabel": {"en": "Median (CAD millions)", "es": "Mediana (millones CAD)"},
    "ins_2_median_ylabel": {"en": "Legal type", "es": "Tipo legal"},
    "ins_3_title": {"en": "3️⃣ Older isn't cheaper — it's the opposite", "es": "3️⃣ Más antiguo NO significa más barato — al revés"},
    "ins_3_text": {
        "en": "Properties built **before 1960** are valued ~2x higher than those built after 1970. This isn't about the buildings — it's about the **land** in established neighbourhoods.",
        "es": "Las propiedades construidas **antes de 1960** valen ~2x más que las construidas después de 1970. No es por el edificio — es por el **terreno** en barrios establecidos."
    },
    "ins_3_xlabel": {"en": "Decade built", "es": "Década de construcción"},
    "ins_3_ylabel": {"en": "Median value (CAD millions)", "es": "Valor mediano (millones CAD)"},
    "ins_4_title": {"en": "4️⃣ The market is heavily right-skewed", "es": "4️⃣ El mercado tiene una fuerte asimetría"},
    "ins_4_text": {
        "en": "Vancouver's property values follow a long-tail distribution. Most properties cluster around $1-2M, but a small share extends well into the millions.",
        "es": "Los valores en Vancouver siguen una distribución de cola larga. La mayoría se concentra entre $1-2M, pero una pequeña parte se extiende a varios millones."
    },
    "ins_4_xlabel": {"en": "Total property value (CAD)", "es": "Valor total (CAD)"},
    "ins_4_median_annotation": {"en": "Median: ${value:,.0f}", "es": "Mediana: ${value:,.0f}"},
    "ins_summary_title": {"en": "🧠 What this means for the model", "es": "🧠 Qué implica esto para el modelo"},
    "ins_summary_text": {
        "en": "These four insights shaped key modeling decisions:\n\n- **Log-transformed target** to handle the right-skewed distribution\n- **Tree-based models** (XGBoost, Random Forest) to capture non-linear age patterns\n- **Neighbourhood** as the primary categorical feature\n- **Legal type** as the strongest single predictor (77% feature importance)\n\nThe model achieves **R² = 0.80** on a held-out test set, with **MAE = $376K**.",
        "es": "Estos cuatro hallazgos guiaron decisiones clave del modelo:\n\n- **Target log-transformado** para manejar la asimetría\n- **Modelos basados en árboles** (XGBoost, Random Forest) para capturar patrones no lineales de antigüedad\n- **Barrio** como feature categórica principal\n- **Tipo legal** como el predictor individual más fuerte (77% de importancia)\n\nEl modelo alcanza **R² = 0,80** en el conjunto de prueba, con **MAE = $376K**."
    },

    # ============================================================
    # ABOUT PAGE
    # ============================================================
    "about_title": {"en": "👤 About this project", "es": "👤 Acerca del proyecto"},
    "about_project_title": {"en": "📖 The project", "es": "📖 El proyecto"},
    "about_project_text": {
        "en": "**Vancouver Property Value Prediction** is an end-to-end machine learning portfolio project that demonstrates the complete data science workflow:\n\n1. **Data acquisition** from a real-world open data source\n2. **Exploratory data analysis** to extract business insights\n3. **Preprocessing & feature engineering** with documented decisions\n4. **Model training, tuning, and validation** with multiple algorithms\n5. **Productization** through this interactive Streamlit dashboard",
        "es": "**Vancouver Property Value Prediction** es un proyecto de portafolio de ML de principio a fin que demuestra el ciclo completo de data science:\n\n1. **Adquisición de datos** desde una fuente abierta del mundo real\n2. **Análisis exploratorio** para extraer insights de negocio\n3. **Preprocesamiento y feature engineering** con decisiones documentadas\n4. **Entrenamiento, ajuste y validación de modelos** con varios algoritmos\n5. **Productización** a través de este dashboard interactivo en Streamlit"
    },
    "about_author_title": {"en": "👋 About the author", "es": "👋 Sobre el autor"},
    "about_location": {"en": "📍 Vancouver, BC", "es": "📍 Vancouver, BC"},
    "about_bio": {
        "en": "Aspiring Data Scientist with hands-on experience in the full ML lifecycle: from raw data ingestion through model deployment. Currently building a portfolio focused on real-world, business-relevant problems.\n\n**Tech stack:** Python · pandas · scikit-learn · XGBoost · Streamlit · Git · SQL\n\n**Open to opportunities** in Data Science, Data Analytics, and Machine Learning roles in Vancouver and remote-friendly companies.",
        "es": "Aspirante a Data Analyst y Data Scientist con experiencia práctica en el ciclo completo de ML: desde la ingesta de datos crudos hasta el despliegue del modelo. Actualmente construyendo un portafolio enfocado en problemas reales y relevantes para el negocio.\n\n**Stack técnico:** Python · pandas · scikit-learn · XGBoost · Streamlit · Git · SQL\n\n**Abierto a oportunidades** en roles de Data Science, Data Analytics y Machine Learning en Vancouver y empresas remote-friendly."
    },
    "about_tech_title": {"en": "🛠️ Technical details", "es": "🛠️ Detalles técnicos"},
    "about_data_subtitle": {"en": "Data", "es": "Datos"},
    "about_data_text": {
        "en": "- **Source:** [City of Vancouver Open Data Portal](https://opendata.vancouver.ca/explore/dataset/property-tax-report/)\n- **Raw size:** 1.55M rows × 30 columns\n- **Filtered:** 209K rows × 17 columns (year 2026, 1st–99th percentile)\n- **Format:** Parquet (columnar, type-preserving)",
        "es": "- **Fuente:** [Portal de Datos Abiertos de Vancouver](https://opendata.vancouver.ca/explore/dataset/property-tax-report/)\n- **Tamaño bruto:** 1,55M filas × 30 columnas\n- **Filtrado:** 209K filas × 17 columnas (año 2026, percentil 1-99)\n- **Formato:** Parquet (columnar, preserva tipos)"
    },
    "about_model_subtitle": {"en": "Model", "es": "Modelo"},
    "about_model_text": {
        "en": "- **Algorithm:** XGBoost regressor (gradient boosting)\n- **Target:** `log(total_value)`\n- **Features:** 5 (neighbourhood, legal type, zoning, property age, years since improvement)\n- **Tuning:** RandomizedSearchCV with 20 iterations",
        "es": "- **Algoritmo:** Regresor XGBoost (gradient boosting)\n- **Target:** `log(total_value)`\n- **Features:** 5 (barrio, tipo legal, zonificación, antigüedad, años desde renovación)\n- **Tuning:** RandomizedSearchCV con 20 iteraciones"
    },
    "about_perf_subtitle": {"en": "Performance", "es": "Rendimiento"},
    "about_perf_text": {
        "en": "- **R²:** 0.80\n- **MAE:** $376,432 CAD\n- **RMSE:** $857,255 CAD\n- **5-fold CV:** R² = 0.798 ± 0.003 (stable)",
        "es": "- **R²:** 0,80\n- **MAE:** $376.432 CAD\n- **RMSE:** $857.255 CAD\n- **CV 5-fold:** R² = 0,798 ± 0,003 (estable)"
    },
    "about_limits_subtitle": {"en": "Limitations", "es": "Limitaciones"},
    "about_limits_text": {
        "en": "- Designed for mainstream properties (1st–99th percentile)\n- Underestimates luxury properties ($5M+) due to missing physical features\n- Future v2: integrate lot size, square footage, and proximity features",
        "es": "- Diseñado para propiedades típicas (percentil 1-99)\n- Subestima propiedades de lujo ($5M+) por falta de features físicas\n- v2 futura: integrar tamaño del lote, m² y features de proximidad"
    },
    "about_links_title": {"en": "🔗 Links", "es": "🔗 Enlaces"},
    "about_link_code": {"en": "💻 View source code", "es": "💻 Ver código fuente"},
    "about_link_linkedin": {"en": "🔗 Connect on LinkedIn", "es": "🔗 Conectar en LinkedIn"},
    "about_link_data": {"en": "📊 Data source", "es": "📊 Fuente de datos"},
    # ============================================================
    # MAP PAGE
    # ============================================================
    "map_title": {"en": "🗺️ Vancouver Property Map", "es": "🗺️ Mapa de Propiedades Vancouver"},
    "map_subtitle": {
        "en": "Explore median property values across Vancouver neighbourhoods. Darker areas indicate higher prices.",
        "es": "Explora los valores medios de propiedades por barrio. Las áreas más oscuras indican precios más altos."
    },
    "map_filter_legal": {"en": "Filter by legal type", "es": "Filtrar por tipo legal"},
    "map_filter_all": {"en": "All properties", "es": "Todas las propiedades"},
    "map_legend_title": {"en": "Median value (CAD)", "es": "Valor mediano (CAD)"},
    "map_tab_map": {"en": "🗺️ Map", "es": "🗺️ Mapa"},
    "map_tab_data": {"en": "📋 Neighbourhood data", "es": "📋 Datos por barrio"},
    "map_neighbourhood": {"en": "Neighbourhood", "es": "Barrio"},
    "map_median_value": {"en": "Median value", "es": "Valor mediano"},
    "map_property_count": {"en": "Properties", "es": "Propiedades"},
    "map_note": {
        "en": "**Note:** Some neighbourhoods in the data (e.g., Coal Harbour, Yaletown, False Creek) are sub-districts within larger City of Vancouver official boundaries. Properties in those areas are grouped into their parent neighbourhood for mapping.",
        "es": "**Nota:** Algunos barrios en los datos (ej. Coal Harbour, Yaletown, False Creek) son sub-áreas dentro de los límites oficiales de Vancouver. Las propiedades en esas áreas se agrupan en el barrio padre para el mapa."
    },
    "map_mapped": {"en": "properties mapped to official boundaries", "es": "propiedades mapeadas a límites oficiales"},
    "map_unmapped": {"en": "properties not mapped (sub-neighbourhoods under parent areas)", "es": "propiedades no mapeadas (sub-áreas agrupadas en barrios padres)"},

    "about_footer": {
        "en": "Built with Python, scikit-learn, XGBoost, and Streamlit. Source code and full documentation available on GitHub.",
        "es": "Hecho con Python, scikit-learn, XGBoost y Streamlit. Código fuente y documentación completa disponibles en GitHub."
    },
}


def t(key: str, lang: str = "en", **kwargs) -> str:
    """Translate a key to the given language, with optional formatting."""
    text = TRANSLATIONS.get(key, {}).get(lang, key)
    if kwargs:
        try:
            text = text.format(**kwargs)
        except KeyError:
            pass
    return text

# ============================================================
# CATEGORICAL DISPLAY MAPPINGS
# ============================================================

ZONING_DISPLAY = {
    "Commercial": {"en": "Commercial", "es": "Comercial"},
    "Comprehensive Development": {"en": "Comprehensive Development", "es": "Desarrollo Integral"},
    "Historical Area": {"en": "Historical Area", "es": "\u00c1rea Hist\u00f3rica"},
    "Industrial": {"en": "Industrial", "es": "Industrial"},
    "Limited Agriculture": {"en": "Limited Agriculture", "es": "Agricultura Limitada"},
    "Residential": {"en": "Residential", "es": "Residencial"},
    "Residential Inclusive": {"en": "Residential Inclusive", "es": "Residencial Inclusivo"},
    "Residential Rental": {"en": "Residential Rental", "es": "Residencial de Alquiler"},
}

LEGAL_TYPE_DISPLAY = {
    "STRATA": {"en": "STRATA (condo/apartment)", "es": "STRATA (condominio/apartamento)"},
    "LAND": {"en": "LAND (full ownership)", "es": "LAND (propiedad completa)"},
    "Other": {"en": "Other", "es": "Otro"},
    "Unknown": {"en": "Unknown", "es": "Desconocido"},
}


def display_value(original, mapping, lang):
    return mapping.get(original, {}).get(lang, original)