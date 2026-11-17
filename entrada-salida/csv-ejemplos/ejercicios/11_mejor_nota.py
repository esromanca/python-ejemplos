import csv

mejor_alumno = None
mejor_nota = float("-inf")

with open("alumnos.csv", "r", encoding="utf-8", newline="") as fichero:
    lector = csv.DictReader(fichero)

    for alumno in lector:
        nota = float(alumno["nota"])

        if nota > mejor_nota:
            mejor_nota = nota
            mejor_alumno = alumno["nombre"]

if mejor_alumno is None:
    print("No hay alumnos en el fichero.")
else:
    print(f"Mejor alumno: {mejor_alumno}")
    print(f"Nota: {mejor_nota}")
