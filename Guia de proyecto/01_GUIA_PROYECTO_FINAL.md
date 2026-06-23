# Proyecto Final — Guía y checklist

Esto es vuestra carta de presentación de cara a empresas. No es un ejercicio más: es el proyecto que vais a enseñar en una entrevista, y la presentación final la verán empresas. Así que tiene que estar bien hecho y enfocado al producto, no a "lo que hicimos en clase".

## La idea

Coger datos reales, resolver un problema útil con ellos usando lo que habéis aprendido en el bootcamp, y presentarlo como un producto: un repositorio bien documentado más una app o un dashboard.

## Qué tiene que llevar

Tiene que estar todo lo visto en el bootcamp:

- Idea clara y dos datasets (uno del proyecto principal y otro de un plan B con otro proyecto distinto).
- Repositorio en GitHub con estructura ordenada, README y requirements.
- Documentación: qué proyecto es, objetivo, decisiones que tomasteis y resultados.
- Preprocesamiento: limpieza, nulos, tipos, feature engineering.
- EDA con gráficos y conclusiones.
- Un modelo de Machine Learning que encaje con el problema.
- Producto final en PowerBI o Streamlit (el que os tire más).
- Opcional: RAG, Ollama o visión, solo si aporta y encaja en el proyecto.

## Sobre el Machine Learning

No hace falta meter todos los tipos de ML. Hay que elegir el que resuelva vuestro problema:

- Inmobiliaria: regresión para predecir el precio de una vivienda.
- Fútbol: clasificación para predecir qué equipo gana.
- Datos con fechas: series temporales para predecir ventas o demanda.
- Agrupar clientes o productos: clustering.
- Imágenes: visión / YOLO.

La pregunta es siempre la misma: ¿qué cosa útil puedo hacer con estos datos? Ahí está vuestro modelo.

## Los dos datasets (esto se hace hoy)

1. Dataset principal: el de vuestro proyecto estrella.
2. Dataset plan B: otro proyecto distinto, por si el primero falla (datos malos, pocos, mal estructurados...).

Apuntad de dónde los sacáis con su enlace. Fuentes:

- Kaggle: https://www.kaggle.com/datasets
- Google Dataset Search: https://datasetsearch.research.google.com/
- datos.gob.es: https://datos.gob.es/
- HuggingFace Datasets: https://huggingface.co/datasets

## La presentación (para más adelante)

Va enfocada al producto, no al código. Imaginad que se lo enseñáis a una empresa: qué problema resuelve, a quién le sirve, qué insights da, qué predice el modelo. El repositorio es lo que evaluamos los profes (que se vea todo el trabajo); la app o dashboard más el modelo es lo que enseñáis.

## Estructura de repositorio recomendada

```
mi-proyecto-final/
├── README.md              qué es, cómo se ejecuta, resultados
├── requirements.txt
├── data/
│   ├── raw/               datos originales
│   └── processed/         datos limpios
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_preprocesamiento.ipynb
│   └── 03_modelado.ipynb
├── src/                   código reutilizable
├── models/                modelo entrenado (.pkl)
└── app/                   streamlit o dashboard
```

## Checklist

- [ ] Idea de proyecto definida y apuntada
- [ ] Dataset principal encontrado (con enlace)
- [ ] Dataset plan B encontrado (con enlace)
- [ ] Tipo de ML elegido y justificado
- [ ] Herramienta de presentación elegida (Streamlit / PowerBI)
- [ ] Repositorio creado en GitHub
- [ ] README inicial escrito
- [ ] Preprocesamiento de datos
- [ ] EDA con gráficos y conclusiones
- [ ] Modelo entrenado y evaluado
- [ ] App / dashboard funcionando
- [ ] Presentación enfocada al producto

## Recordatorio

Los proyectos anteriores del bootcamp también suman a vuestra experiencia. Si no los habéis subido a GitHub, aprovechad y subidlos.
