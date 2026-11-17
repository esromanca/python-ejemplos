import csv

# El modo "a" añade filas al final sin borrar las anteriores.
with open("productos.csv", "a", newline="", encoding="utf-8") as fichero:
    escritor = csv.writer(fichero)
    escritor.writerow(["Impresora", 89.90, 3])

print("Se ha añadido un producto a productos.csv")
