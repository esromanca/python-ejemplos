import csv

with open("alumnos.csv", "r", encoding="utf-8", newline="") as fichero:
    lector = csv.DictReader(fichero)

    for alumno in lector:
        nota = float(alumno["nota"])

        if nota >= 5:
            resultado = "APROBADO"
        else:
            resultado = "SUSPENSO"

        print(f'{alumno["nombre"]}: {nota} - {resultado}')
