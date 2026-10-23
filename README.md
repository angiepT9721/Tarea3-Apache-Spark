# Tarea 3 - Procesamiento de Datos con Apache Spark

## Descripción del proyecto

Este proyecto desarrolla un ejercicio de procesamiento de datos por lotes (batch) utilizando Apache Spark y PySpark. Se emplea un conjunto de datos abiertos de Colombia sobre las tasas de interés activas por tipo de crédito, con información correspondiente al periodo de enero a octubre de 2026.

El objetivo es limpiar y transformar los datos, realizar un análisis exploratorio y calcular estadísticas descriptivas para comparar las tasas de interés según el tipo de crédito y el mes.

## Fuente de datos

**Conjunto de datos:** Tasas de interés activas por tipo de crédito – Histórico.

**Portal:** Datos Abiertos Colombia.

**Enlace:** https://www.datos.gov.co/Econom-a-y-Finanzas/Tasas-de-inter-s-activas-por-tipo-de-cr-dito-Hist-/w9zh-vetq

El archivo CSV utilizado debe descargarse por separado y ubicarse en la ruta configurada en el código.

## Archivos del proyecto

- `tarea3_batch.py`: carga, limpieza, transformación y análisis exploratorio de los datos mediante Apache Spark.
- `tarea3_muestra.py`: genera una muestra de 10.000 registros por cada mes, para un total de 100.000 registros.
- `resumen_muestra.py`: calcula el promedio de las tasas de interés mensuales a partir de la muestra equilibrada.
- `grafica_mensual.py`: genera una gráfica de los promedios mensuales calculados.

## Tecnologías utilizadas

- Python 3.
- Apache Spark.
- PySpark.
- Matplotlib.
- Ubuntu Linux.

## Ejecución

1. Instalar Python, Apache Spark, PySpark y Matplotlib.
2. Descargar el conjunto de datos desde el enlace indicado.
3. Revisar las rutas de entrada y salida configuradas en los scripts y ajustarlas al entorno local.
4. Ejecutar el procesamiento por lotes:

   ```bash
   spark-submit tarea3_batch.py
   ```

5. Generar la muestra equilibrada por mes:

   ```bash
   spark-submit tarea3_muestra.py
   ```

6. Calcular el resumen mensual de la muestra:

   ```bash
   spark-submit resumen_muestra.py
   ```

7. Generar la gráfica mensual:

   ```bash
   python3 grafica_mensual.py
   ```

Los scripts de análisis requieren que existan los archivos de entrada y las carpetas de resultados esperadas por cada programa. Las rutas deben adaptarse si se ejecuta el proyecto en otro equipo.

## Consideraciones metodológicas

La muestra utilizada para la comparación mensual contiene 10.000 registros por mes, de enero a octubre de 2026. La selección se realiza ordenando los registros y tomando los primeros 10.000 de cada mes; por tanto, no corresponde a una muestra aleatoria y puede presentar sesgos.

Los resultados describen los datos procesados y deben interpretarse teniendo en cuenta las características y limitaciones de la muestra.

## Autoría

**Angie Paola Triana Fernandez**

Actividad académica correspondiente a la Tarea 3: Procesamiento de Datos con Apache Spark, UNAD.
