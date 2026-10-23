
from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col, trim, avg, min, max, count,
    date_format, when, sum
)

# Crear la sesión de Spark
spark = SparkSession.builder \
    .appName("Tarea3_Procesamiento_Batch") \
    .getOrCreate()

# Cargar el archivo CSV
ruta = "/home/vboxuser/tasas_enero_octubre_2026.csv"

df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .option("encoding", "UTF-8") \
    .csv(ruta)

print("Total de registros:", df.count())
print("Total de columnas:", len(df.columns))

# Revisar valores nulos
df.select([
    sum(when(col(c).isNull(), 1).otherwise(0)).alias(c)
    for c in df.columns
]).show(truncate=False)

# Seleccionar columnas para el análisis
df_limpio = df.select(
    "fecha_corte",
    "nombre_entidad",
    "tipo_de_persona",
    "sexo",
    "tama_o_de_empresa",
    "tipo_de_cr_dito",
    "producto_de_cr_dito",
    "tasa_efectiva_promedio",
    "montos_desembolsados",
    "numero_de_creditos",
    "codigo_municipio"
)

# Quitar espacios sobrantes de algunos campos de texto
df_limpio = df_limpio.withColumn(
    "nombre_entidad", trim(col("nombre_entidad"))
).withColumn(
    "tipo_de_cr_dito", trim(col("tipo_de_cr_dito"))
)

# Estadísticas de las tasas
df_limpio.select("tasa_efectiva_promedio") \
    .describe().show()

# Resumen por tipo de crédito
resumen_creditos = df_limpio.groupBy("tipo_de_cr_dito").agg(
    count("*").alias("cantidad_registros"),
    avg("tasa_efectiva_promedio").alias("tasa_promedio"),
    min("tasa_efectiva_promedio").alias("tasa_minima"),
    max("tasa_efectiva_promedio").alias("tasa_maxima")
)

resumen_creditos.orderBy(
    "tasa_promedio", ascending=False
).show(truncate=False)

# Resumen mensual
resumen_mensual = df_limpio.withColumn(
    "mes", date_format("fecha_corte", "yyyy-MM")
).groupBy("mes").agg(
    count("*").alias("cantidad_registros"),
    avg("tasa_efectiva_promedio").alias("tasa_promedio")
).orderBy("mes")

resumen_mensual.show(truncate=False)

# Guardar resultados
resumen_creditos.coalesce(1).write \
    .mode("overwrite").option("header", True) \
    .csv("/home/vboxuser/resumen_creditos")

resumen_mensual.coalesce(1).write \
    .mode("overwrite").option("header", True) \
    .csv("/home/vboxuser/resumen_mensual")

print("Procesamiento por lotes finalizado.")
