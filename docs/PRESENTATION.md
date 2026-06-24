# Vancouver Property Value Prediction — Presentación

> 📌 *Enfocada al producto y al negocio, no al código. Esto es lo que verán las empresas.*

---

## Slide 1 — Portada

**Vancouver Property Value Prediction**
*¿Cuánto vale realmente una propiedad en Vancouver?*

Rafael Carrillo Mirabal
GitHub: [racarrillo2/vancouver-property-value-prediction](https://github.com/racarrillo2/vancouver-property-value-prediction)
Streamlit App: [vancouver-property-value-prediction.streamlit.app](https://vancouver-property-value-prediction.streamlit.app)

---

## Slide 2 — El Problema

**Vancouver tiene uno de los mercados inmobiliarios más caros de Norteamérica.**

- El precio mediano de una propiedad supera los $1.5M CAD
- Hay una disparidad brutal entre barrios: hasta **7x** de diferencia
- Compradores e inversores no tienen una herramienta objetiva para saber si una propiedad está sobrevalorada
- Las tasaciones profesionales son lentas y caras

**¿A quién le sirve esto?**
- **Compradores de vivienda** → saber si están pagando un precio justo
- **Agentes inmobiliarios** → fundamentar recomendaciones con datos
- **Inversores** → identificar propiedades infravaloradas por barrio

---

## Slide 3 — Los Datos

**Fuente:** City of Vancouver — Property Tax Report (Open Data Portal)

| Característica | Valor |
|---|---|
| Formato | Parquet |
| Filas | ~1.55M registros (2020–2026) |
| Columnas | 30 variables |
| Tamaño | 134 MB en disco / 691 MB en memoria |
| Cobertura | Todas las propiedades de Vancouver |

**Variables clave:**
- `current_land_value` + `current_improvement_value` → valor total (target)
- `neighbourhood_code` → barrio (3 dígitos)
- `legal_type` → STRATA / LAND / OTHER
- `zoning_classification` → zonificación
- `year_built` → año de construcción

**Enriquecimiento:** Cruzamos códigos de barrio con nombres reales (Shaughnessy, Kerrisdale, etc.) para hacer el análisis interpretable.

---

## Slide 4 — EDA: Los 3 Insights Clave

### 1. El barrio lo es todo
Diferencia de hasta **7x** entre el barrio más caro (Shaughnessy ~$4.4M mediana) y el más barato (East Hastings ~$0.65M). La ubicación es el predictor #1.

### 2. STRATA vs LAND: dos mundos distintos
Las propiedades STRATA (condominios/apartamentos) y LAND (terrenos con casa) tienen estructuras de precio fundamentalmente diferentes. El modelo necesita tratarlas por separado.

### 3. La edad importa... pero no linealmente
Propiedades anteriores a 1960 valen ~2x más que las construidas entre 1970–2000. Hay un "escalón" en el valor que no sigue una tendencia continua.

*Insight adicional:* Vancouver es un mercado **land-driven** — el valor del terreno representa ~70% del valor total en propiedades LAND.

---

## Slide 5 — Modelo: XGBoost Regressor

**¿Por qué este modelo?**

| Modelo | R² (test) | MAE |
|---|---|---|
| Baseline (media) | -0.00 | $937K |
| Regresión Lineal | 0.69 | $466K |
| Random Forest | 0.78 | $393K |
| XGBoost | 0.80 | $379K |
| **XGBoost (tuned)** | **0.80** | **$376K** |

**XGBoost gana porque:**
- Maneja bien datos tabulares con mezcla de categóricas y numéricas
- Captura relaciones no lineales (como el escalón de edad)
- Es robusto a outliers y valores nulos
- Es el estándar industrial para este tipo de problema

**Validación:** 5-fold cross-validation — R² estable en **0.798 ± 0.003**

---

## Slide 6 — Feature Importance: ¿Qué impulsa el precio?

1. **Legal type (STRATA vs LAND)** — **50.0%** ⚡
2. **Neighbourhood** — **19.6%**
3. **Years since last improvement** — 11.5%
4. **Zoning classification** — 11.0%
5. **Property age** — 7.9%

> *Nota: Estos valores usan **permutation importance** (scikit-learn), que es más fiable que la importancia nativa de XGBoost. La importancia nativa diluía neighbourhood al dividirlo en 30+ columnas one-hot, mostrando erróneamente 77% para legal_type.*

**Conclusión para el negocio:**
~70% del valor de una propiedad en Vancouver se explica por **qué tipo de propiedad es** + **dónde está ubicada**. Legal type es **~2.55× más importante** que neighbourhood. Las características físicas (año, mejoras) tienen un impacto marginal.

Esto tiene sentido: en un mercado con escasez de suelo, la ubicación y el tipo de tenencia son los verdaderos drivers.

---

## Slide 7 — Demo en Vivo

**Streamlit Dashboard** — [vancouver-property-value-prediction.streamlit.app](https://vancouver-property-value-prediction.streamlit.app)

La app permite:

1. **Predictor** → formulario donde ingresas tipo, barrio, año y zonificación → obtienes una estimación instantánea con rango de confianza
2. **Insights** → 4 gráficos interactivos del EDA explicados en lenguaje sencillo
3. **About** → contexto del proyecto, métricas y limitaciones
4. **Idioma** → toggle Español / English en cualquier momento

*Demo en vivo: predecir una propiedad STRATA en Coal Harbour vs una LAND en Shaughnessy*

> ⚠️ Plan de contingencia: si la demo en vivo falla por internet, tengo capturas de pantalla preparadas.

---

## Slide 8 — Limitaciones y Próximos Pasos

### Limitaciones actuales
- **Sin datos físicos:** No tenemos sqft, número de habitaciones, lot size, view — esto limitaría el MAE
- **Rango acotado:** El modelo se entrenó con el percentil 1–99 (excluyendo el 1% de valores extremos), lo que limita la precisión en propiedades de lujo >~$5M
- **Solo Vancouver:** no aplica a otras ciudades sin reentrenar

### Próximos pasos (si fuera producción)
1. Integrar datasets de BC Assessment con características físicas
2. Añadir features de proximidad (parques, escuelas, transit)
3. Modelo por separado para STRATA vs LAND
4. API REST con FastAPI para que terceros la integren
5. Actualización automática con cada nuevo Property Tax Report

---

## Slide 9 — Q&A: Preguntas frecuentes preparadas

**Q: ¿Por qué XGBoost y no una red neuronal?**
R: Para datos tabulares estructurados, XGBoost iguala o supera a redes neuronales con mucho menos costo computacional y más interpretabilidad. Una NN sería overkill aquí.

**Q: ¿Qué harías diferente con más tiempo?**
R: 1) Conseguir datos físicos (sqft, habitaciones) para bajar el MAE. 2) Hacer un modelo específico para propiedades >$5M. 3) Añadir SHAP values para explicar predicciones individuales.

**Q: ¿Cómo lo pondrías en producción?**
R: API con FastAPI → endpoint `/predict` → el dashboard de Streamlit consume la API. Docker + despliegue en Railway o AWS. Actualización programada con cada nuevo Property Tax Report.

**Q: ¿Cómo evitaste el data leakage?**
R: Excluí `tax_levy` y las columnas `previous_*` del entrenamiento. El `tax_levy` se calcula a partir del valor de la propiedad, así que usarlo como feature inflaría artificialmente el R².

---

## Slide 10 — Cierre

**Proyecto completo:** 7 fases — desde datos crudos hasta dashboard interactivo desplegado

**Repo:** [github.com/racarrillo2/vancouver-property-value-prediction](https://github.com/racarrillo2/vancouver-property-value-prediction)

**App:** [vancouver-property-value-prediction.streamlit.app](https://vancouver-property-value-prediction.streamlit.app)

**Contacto:** Rafael Carrillo — [LinkedIn](https://www.linkedin.com/in/rafael-carrillo-mirabal/?locale=en)

> *"Data talks, but a story sells. This is the story of Vancouver's real estate market, told through 1.55 million data points."*

---

## 📋 Notas para el presentador

- **Duración:** 5 minutos — 30 segundos por slide
- **NO muestres código** — nadie en una empresa quiere ver tu Jupyter Notebook
- **La demo es lo más importante** — asegúrate de que la app funciona y tienes internet