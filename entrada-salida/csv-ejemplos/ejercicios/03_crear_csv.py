import csv

# El modo "w" crea el fichero o sobrescribe su contenido si ya existe.
with open("productos.csv", "w", newline="", encoding="utf-8") as fichero:
    escritor = csv.writer(fichero)

    escritor.writerow(["producto", "precio", "stock"])
    escritor.writerow(["Teclado", 25.50, 10])
    escritor.writerow(["Ratón", 15.90, 20])
    escritor.writerow(["Monitor", 150.00, 5])

print("Se ha creado productos.csv")
