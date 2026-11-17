import csv

suma = 0.0
contador = 0

with open("alumnos.csv", "r", encoding="utf-8", newline="") as fichero:
    lector = csv.DictReader(fichero)

    for alumno in lector:
        suma += float(alumno["nota"])
        contador += 1

if contador > 0:
    media = suma / contador
    print(f"Nota media de la clase: {media:.2f}")
else:
    print("El fichero no contiene alumnos.")
