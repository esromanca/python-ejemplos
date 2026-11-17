import csv

# DictReader usa la primera fila como claves de cada diccionario.
with open("alumnos.csv", "r", encoding="utf-8", newline="") as fichero:
    lector = csv.DictReader(fichero)

    for alumno in lector:
        print("Nombre:", alumno["nombre"])
        print("Edad:", alumno["edad"])
        print("Nota:", alumno["nota"])
        print("---")
