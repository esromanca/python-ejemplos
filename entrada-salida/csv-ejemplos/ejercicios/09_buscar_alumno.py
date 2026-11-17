import csv

nombre_buscar = input("Nombre del alumno que quieres buscar: ").strip()
encontrado = False

with open("alumnos.csv", "r", encoding="utf-8", newline="") as fichero:
    lector = csv.DictReader(fichero)

    for alumno in lector:
        if alumno["nombre"].casefold() == nombre_buscar.casefold():
            print("Alumno encontrado:")
            print("Nombre:", alumno["nombre"])
            print("Edad:", alumno["edad"])
            print("Nota:", alumno["nota"])
            encontrado = True
            break

if not encontrado:
    print("No se ha encontrado ese alumno.")
