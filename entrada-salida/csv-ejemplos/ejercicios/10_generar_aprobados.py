import csv

# Leemos el fichero original y escribimos los aprobados en otro fichero.
with open("alumnos.csv", "r", encoding="utf-8", newline="") as origen:
    lector = csv.DictReader(origen)

    with open("aprobados.csv", "w", newline="", encoding="utf-8") as destino:
        campos = ["nombre", "edad", "nota"]
        escritor = csv.DictWriter(destino, fieldnames=campos)
        escritor.writeheader()

        for alumno in lector:
            if float(alumno["nota"]) >= 5:
                escritor.writerow(alumno)

print("Se ha generado aprobados.csv")
