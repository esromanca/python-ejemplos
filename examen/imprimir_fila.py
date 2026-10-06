import csv
with open('datos.csv', newline='') as f:
    lector = csv.reader(f, delimiter=',',quotechar='"', escapechar='\\')
    for fila in lector:
        print(fila)
        print(fila[1])
