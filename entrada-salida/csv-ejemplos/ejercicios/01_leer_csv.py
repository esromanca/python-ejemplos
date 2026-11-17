import csv

# Abrimos el fichero en modo lectura.
# encoding="utf-8" permite leer correctamente tildes y ñ.
with open("alumnos.csv", "r", encoding="utf-8", newline="") as fichero:
    lector = csv.reader(fichero)

    # Cada fila es una lista de cadenas.
    for fila in lector:
        print(fila)
