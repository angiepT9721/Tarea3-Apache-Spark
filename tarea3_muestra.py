
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, date_format, row_number
from pyspark.sql.window import Window

spark = SparkSession.builder \
    .appName("Tarea3_Muestra_Equilibrada") \
    .getOrCreate()

ruta = "/home/vboxuser/tasas_enero_octubre_2026.csv"

df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .option("encoding", "UTF-8") \
    .csv(ruta)

# Crear una columna con el mes de cada registro
df_mes = df.withColumn(
    "mes", date_format(col("fecha_corte"), "yyyy-MM")
)

# Orden reproducible dentro de cada mes
ventana = Window.partitionBy("mes").orderBy(
    col("fecha_corte"),
    col("codigo_entidad"),
    col("codigo_municipio")
)

# Seleccionar hasta 10.000 registros por mes
muestra = df_mes.withColumn(
    "numero_fila", row_number().over(ventana)
).filter(
    col("numero_fila") <= 10000
).drop(
    "numero_fila", "mes"
)

# Guardar en una nueva carpeta, sin modificar el CSV original
muestra.coalesce(1).write \
    .mode("overwrite") \
    .option("header", True) \
    .csv("/home/vboxuser/muestra_equilibrada")

print("Registros seleccionados:", muestra.count())

muestra.withColumn(
    "mes", date_format(col("fecha_corte"), "yyyy-MM")
).groupBy("mes").count().orderBy("mes").show()

print("Muestra equilibrada creada correctamente.")

spark.stop()
