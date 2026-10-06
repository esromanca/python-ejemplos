import csv
with open('datos.csv', newline='') as f:
    lector = csv.reader(f, delimiter=',', escapechar='\\')
    for fila in lector:
        print(fila)
