import csv
try:
  corte = float(input ("escribe la nota de corte"))
except:
  print("mete un número decimal")

with open("alumnos.csv", "r", encoding="utf-8", newline="") as fichero:
    lector = csv.reader(fichero)
    next(lector)
    for alumno in lector:
        nota = float(alumno[2])

        if nota >= corte:
            resultado = "APROBADO"
        else:
            resultado = "SUSPENSO"

        print(f'{alumno[0]}: {nota} - {resultado}')
