import csv

with open("alumnos.csv", "r", encoding="utf-8", newline="") as fichero:
    lector = csv.reader(fichero)

    # next() consume la primera fila, que contiene los nombres de columnas.
    next(lector)

    for fila in lector:
        nombre = fila[0]
        edad = int(fila[1])       # Los datos CSV se leen inicialmente como texto.
        nota = float(fila[2])

        print(f"{nombre}: {edad} años, nota {nota}")
