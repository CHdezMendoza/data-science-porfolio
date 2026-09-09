# Data Science Portfolio

¡Bienvenido a mi portafolio de análisis de datos!

Soy Carlos Mendoza y este repositorio contiene una colección de proyectos que demuestran mis habilidades en **Python**, **Pandas**, **Matplotlib** y **análisis exploratorio de datos**. Cada carpeta contiene un proyecto independiente con su propio conjunto de datos, script de análisis y gráficos generados.

## Habilidades demostradas

- Carga, limpieza y transformación de datos con Pandas.
- Visualización de datos con Matplotlib (barras, histogramas, dispersión, boxplots, mapas de calor, series temporales).
- Análisis exploratorio y extracción de insights.
- Manejo de datos temporales y cálculo de métricas (retornos, medias móviles).
- Procesamiento básico de texto y análisis de sentimiento con reglas.

## Proyectos

### 1. Análisis de Supervivencia en el Titanic
- **Carpeta:** `titanic/`
- **Dataset:** Titanic (train.csv)
- **Objetivo:** Identificar factores que influyeron en la supervivencia de los pasajeros.
- **Resultados clave:**
  - Las mujeres tuvieron una tasa de supervivencia del 74%, frente al 19% de los hombres.
  - La primera clase tuvo la mayor tasa de supervivencia (~63%).
  - Los niños tuvieron mayor probabilidad de sobrevivir que los adultos.
- **Gráficos:** tasa de supervivencia por sexo, clase, distribución de edades, relación edad-tarifa.

### 2. Ventas de Videojuegos
- **Carpeta:** `videojuegos/`
- **Dataset:** Video Game Sales (vgsales.csv)
- **Objetivo:** Explorar tendencias de ventas por plataforma, género y año.
- **Resultados clave:**
  - PS2 es la plataforma con más ventas acumuladas.
  - El género Action domina con ~1,750 millones de unidades.
  - Las ventas alcanzaron su pico en 2008 y luego declinaron.
  - Nintendo es el publisher líder.
- **Gráficos:** top 10 plataformas, ventas por género, evolución anual.

### 3. Temperaturas Globales
- **Carpeta:** `temperaturas/`
- **Dataset:** Global Temperature Time Series (mensual, 1850-2020)
- **Objetivo:** Analizar la evolución de la temperatura media global.
- **Resultados clave:**
  - Clara tendencia ascendente desde finales del siglo XIX.
  - La media móvil de 5 años suaviza la variabilidad y confirma el calentamiento.
- **Gráficos:** línea temporal con media móvil.

### 4. Precios de Acciones (Apple y Tesla)
- **Carpeta:** `acciones/`
- **Dataset:** Descargado con `yfinance` (últimos 3 años)
- **Objetivo:** Comparar rendimiento y volatilidad de dos acciones tecnológicas.
- **Resultados clave:**
  - Tesla presenta mayor volatilidad diaria.
  - Apple tuvo mayor rendimiento total en el período.
- **Gráficos:** precios normalizados, histogramas de retornos diarios.

### 5. Películas IMDb
- **Carpeta:** `imdb/`
- **Dataset:** IMDB-Movie-Data.csv (1000 películas)
- **Objetivo:** Analizar ratings e ingresos por género.
- **Resultados clave:**
  - Géneros mejor valorados: Drama, Biografía.
  - Correlación positiva moderada entre rating y revenue.
- **Gráficos:** barras de rating por género, boxplots, scatter rating vs ingresos.

### 6. Análisis de Reseñas de Alexa
- **Carpeta:** `alexa_reviews/`
- **Dataset:** Sintético (reviews de Amazon Alexa)
- **Objetivo:** Procesamiento de texto y análisis de sentimiento básico.
- **Resultados clave:**
  - Palabras frecuentes: love, great, good, product, excellent.
  - El clasificador con reglas logra identificar la mayoría de positivos, pero falla en negaciones.
- **Gráficos:** frecuencia de palabras, comparación de sentimiento.

### 7. Precios de Vivienda en California
- **Carpeta:** `housing/`
- **Dataset:** California Housing (housing.csv)
- **Objetivo:** Identificar factores correlacionados con el valor mediano de la vivienda.
- **Resultados clave:**
  - `median_income` es la variable con mayor correlación positiva (0.69).
  - Se observa un tope artificial en $500,000 que limita la correlación.
- **Gráficos:** mapa de calor, scatter ingreso vs valor, distribución geográfica.

### 8. Pingüinos Palmer
- **Carpeta:** `penguins/`
- **Dataset:** Palmer Penguins (penguins.csv)
- **Objetivo:** Explorar relaciones entre medidas corporales y diferencias entre especies.
- **Resultados clave:**
  - Flipper length y body mass altamente correlacionados (0.87).
  - La especie Gentoo es la más distinta en tamaño.
- **Gráficos:** mapa de calor, scatter por especie, boxplots.

### 9. COVID-19: Casos Confirmados por País
- **Carpeta:** `covid_analysis/`
- **Dataset:** John Hopkins University (time series global)
- **Objetivo:** Comparar la evolución de casos en varios países y calcular métricas de crecimiento.
- **Resultados clave:**
  - US, India y Brasil tuvieron duplicaciones más rápidas al inicio.
  - México mostró dos picos importantes en 2022.
- **Gráficos:** casos confirmados (escala log), nuevos casos diarios con media móvil.

## Herramientas utilizadas

- Python 3.9
- Pandas
- Matplotlib
- NumPy
- yfinance
- requests

## Cómo ejecutar los proyectos

Cada carpeta contiene un script `.py` que puede ejecutarse de forma independiente.

## Contacto
[Carlos Mendoza] - [carlosmendoza4@me.com] - [https://www.linkedin.com/in/carlos-hern%C3%A1ndez-mendoza-6539a982/]
