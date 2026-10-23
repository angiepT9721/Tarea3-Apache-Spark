import csv
import glob
import matplotlib.pyplot as plt

archivo = glob.glob("/home/vboxuser/resumen_muestra_mensual/part-*.csv")[0]

meses = []
tasas = []

with open(archivo, "r", encoding="utf-8") as f:
    lector = csv.DictReader(f)
    for fila in lector:
        meses.append(fila["mes"])
        tasas.append(float(fila["tasa_promedio"]))

plt.figure(figsize=(10, 5))
plt.plot(meses, tasas, marker="o")
plt.title("Tasa de interés promedio por mes - 2026")
plt.xlabel("Mes")
plt.ylabel("Tasa efectiva promedio")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("/home/vboxuser/grafica_mensual.png", dpi=150)
print("Gráfica guardada en /home/vboxuser/grafica_mensual.png")
