import csv

# Algunos CSV usan punto y coma en lugar de coma.
# Este ejemplo crea primero un pequeño fichero de muestra.
with open("alumnos_es.csv", "w", newline="", encoding="utf-8") as fichero:
    escritor = csv.writer(fichero, delimiter=";")
    escritor.writerow(["nombre", "edad", "nota"])
    escritor.writerow(["Ana", 20, 8.5])
    escritor.writerow(["Luis", 21, 7.2])

# Para leerlo, indicamos el mismo delimitador.
with open("alumnos_es.csv", "r", encoding="utf-8", newline="") as fichero:
    lector = csv.reader(fichero, delimiter=";")
    for fila in lector:
        print(fila)
