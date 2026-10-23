from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, count, date_format

spark = SparkSession.builder \
    .appName("Tarea3_Resumen_Muestra") \
    .getOrCreate()

ruta = "/home/vboxuser/muestra_equilibrada/part-*.csv"

df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .option("encoding", "UTF-8") \
    .csv(ruta)

resumen = df.withColumn(
    "mes", date_format(col("fecha_corte"), "yyyy-MM")
).groupBy("mes").agg(
    count("*").alias("cantidad_registros"),
    avg("tasa_efectiva_promedio").alias("tasa_promedio")
).orderBy("mes")

resumen.show(20, truncate=False)

resumen.coalesce(1).write \
    .mode("overwrite") \
    .option("header", True) \
    .csv("/home/vboxuser/resumen_muestra_mensual")

print("Resumen mensual de la muestra generado correctamente.")

spark.stop()
