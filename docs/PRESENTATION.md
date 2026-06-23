# Vancouver Property Value Prediction — Presentación

> 📌 *Enfocada al producto y al negocio, no al código. Esto es lo que verán las empresas.*

---

## Slide 1 — Portada

**Vancouver Property Value Prediction**  
*¿Cuánto vale realmente una propiedad en Vancouver?*

Rafael Carrillo Mirabal  
GitHub: [racarrillo2/vancouver-property-value-prediction](https://github.com/racarrillo2/vancouver-property-value-prediction)  
Streamlit App: [link pendiente de deploy]

---

## Slide 2 — El Problema

**Vancouver tiene uno de los mercados inmobiliarios más caros de Norteamérica.**

- El precio promedio de una vivienda supera los $1.2M CAD
- Hay una gran disparidad entre barrios: hasta 7x de diferencia
- Compradores e inversores no tienen una herramienta objetiva para saber si una propiedad está sobrevalorada
- Las tasaciones son lentas y caras

**¿A quién le sirve esto?**
- Compradores de vivienda → saber si están pagando un precio justo
- Agentes inmobiliarios → fundamentar recomendaciones con datos
- Inversores → identificar propiedades infravaloradas por barrio

---

## Slide 3 — Los Datos

**Fuente:** City of Vancouver — Property Tax Report (Open Data Portal)

| Característica | Valor |
|---|---|
| Formato | Parquet |
| Filas | ~1.55M registros (2017–2026) |
| Columnas | 30 variables |
| Tamaño | 134 MB en disco / 691 MB en memoria |
| Cobertura | Todas las propiedades de Vancouver |

**Variables clave:**
- `current_land_value` + `current_improvement_value` → valor total (target)
- `neighbourhood_code` → barrio (3 dígitos)
- `legal_type` → STRATA / LAND / OTHER
- `zoning_classification` → zonificación
- `year_built` → año de construcción

**Enriquecimiento:** Cruzamos códigos de barrio con el dataset "Local Area Boundary" para tener nombres reales (Shaughnessy, Kerrisdale, etc.)

---

## Slide 4 —EDA: Los 3 Insights Clave

### 1. El barrio lo es todo
Diferencia de hasta **7x** entre el barrio más caro (Shaughnessy ~$3.1M) y el más barato (Strathcona ~$450K). El código postal es el predictor #1.

### 2. STRATA vs LAND: dos mundos distintos
Las propiedades STRATA (condominios) valen ~$700K promedio; las LAND (terrenos con casa) ~$2.3M. El modelo necesita tratar estos grupos por separado.

### 3. La edad importa... pero no linealmente
Propiedades anteriores a 1970 tienen una distribución de precio muy distinta a las posteriores. Hay un "escalón" en el valor que no sigue una tendencia continua.

*Insight adicional:* Vancouver es un mercado **land-driven** — el valor del terreno representa ~70% del valor total en propiedades LAND.

---

## Slide 5 — Modelo: XGBoost Regressor

**¿Por qué este modelo?**

| Modelo | R² (test) | MAE |
|---|---|---|
| Regresión Lineal | 0.74 | $450K |
| Random Forest | 0.76 | $400K |
| **XGBoost (tuned)** | **0.80** | **$376K** |

**XGBoost gana porque:**
- Maneja bien datos tabulares con mezcla de categóricas y numéricas
- Captura relaciones no lineales (como el escalón de edad)
- Es robusto a outliers y valores nulos
- Es el estándar industrial en competiciones de Kaggle para este tipo de problema

**Validación:** 5-fold cross-validation — R² estable en 0.798 ± 0.003

---

## Slide 6 — Feature Importance: ¿Qué impulsa el precio?

1. **Legal type (STRATA vs LAND)** — **77% de importancia** ⚡
2. **Neighbourhood** — 13%
3. **Zoning classification** — 5%
4. **Property age** — 3%
5. **Years since last improvement** — 2%

**Conclusión para el negocio:**  
El 90% del valor de una propiedad en Vancouver se explica por **qué tipo de propiedad es** + **dónde está ubicada**. Las características físicas (año, mejoras) tienen un impacto marginal.

Esto tiene sentido: en un mercado con escasez de suelo, la ubicación y el tipo de tenencia son los verdaderos drivers.

---

## Slide 7 — Demo en Vivo

**Streamlit Dashboard** — [enlace a app desplegada]

La app permite:

1. **Explorar datos** → mapa interactivo de Vancouver con precios por barrio
2. **Predecir precio** → formulario donde ingresas tipo, barrio, año y zonificación → obtienes una estimación instantánea
3. **Ver insights** → gráficos clave del EDA explicados en lenguaje sencillo
4. **Idioma** → toggle Español / English

*Demo: predecir una propiedad STRATA en Kitsilano de 1990 vs una LAND en Shaughnessy de 1960*

---

## Slide 8 — Limitaciones y Próximos Pasos

### Limitaciones actuales
- **Sin datos físicos:** No tenemos sqft, número de habitaciones, lot size, view — esto limitaría el MAE
- **Subestima propiedades de lujo** (>$5M): faltan features como vista al mar, acabados, tamaño de terreno
- **Solo Vancouver:** no aplica a otras ciudades sin reentrenar

### Próximos pasos (si fuera producción)
1. Integrar datasets de BC Assessment con características físicas
2. Añadir features de proximidad (parques, escuelas, transit)
3. Modelo por separado para STRATA vs LAND
4. API para que agentes inmobiliarios la integren en sus herramientas
5. Actualización automática con cada nuevo año fiscal

---

## Slide 9 — Preguntas para la audiencia / Inversores

**Preguntas frecuentes y respuestas preparadas:**

**Q: ¿Por qué XGBoost y no una red neuronal?**
R: Para datos tabulares estructurados, XGBoost iguala o supera a redes neuronales con mucho menos costo computacional y más interpretabilidad. Una NN sería overkill aquí.

**Q: ¿Qué harías diferente con más tiempo?**
R: 1) Conseguir datos físicos (sqft, habitaciones) para bajar el MAE. 2) Hacer un modelo específico para propiedades >$5M. 3) Añadir SHAP values para explicar predicciones individuales.

**Q: ¿Cómo lo pondrías en producción?**
R: API con FastAPI → endpoint `/predict` → el dashboard de Streamlit consume la API. Docker + despliegue en Railway o AWS. Actualización programada con cada nuevo Property Tax Report.

---

## Slide 10 — Cierre

**Proyecto:** Fin de 6 fases completadas — desde datos crudos hasta dashboard interactivo

**Repo:** [github.com/racarrillo2/vancouver-property-value-prediction](https://github.com/racarrillo2/vancouver-property-value-prediction)

**App:** [link a Streamlit Cloud]

**Contacto:** Rafael Carrillo — [LinkedIn](https://www.linkedin.com/in/rafael-carrillo-mirabal/?locale=en)

> "Data talks, but a story sells. This is the story of Vancouver's real estate market, told through 1.5 million data points."

---

## 📋 Notas para el presentador

- **Duración:** 5 minutos — 30 segundos por slide
- **NO muestres código** — nadie en una empresa quiere ver tu Jupyter Notebook
- **La demo es lo más importante** — asegúrate de que la app funciona y tienes internet
- **Si falla la demo**, ten capturas de pantalla en los slides de backup
- **Termina con una pregunta** para abrir conversación, no con "gracias"
- **Practica en voz alta** 3 veces mínimo antes del Jueves
