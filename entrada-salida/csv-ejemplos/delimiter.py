import csv

with open("delimiter.txt",newline="") as f:
    lector = csv.reader(f, delimiter=',', quotechar='"',escapechar='\\')
    for fila in lector:
        print("PRIMER CAMPO: ",fila[0],"SEGUNDO CAMPO: ",fila[1])
