import csv

alumnos_nuevos = [
    {"nombre": "Alicia", "edad": 20, "nota": 8.7},
    {"nombre": "Bruno", "edad": 22, "nota": 6.3},
    {"nombre": "Celia", "edad": 19, "nota": 9.0},
]

with open("alumnos_nuevos.csv", "w", newline="", encoding="utf-8") as fichero:
    campos = ["nombre", "edad", "nota"]
    escritor = csv.DictWriter(fichero, fieldnames=campos)

    escritor.writeheader()       # Escribe la fila de cabecera.
    escritor.writerows(alumnos_nuevos)

print("Se ha creado alumnos_nuevos.csv")
