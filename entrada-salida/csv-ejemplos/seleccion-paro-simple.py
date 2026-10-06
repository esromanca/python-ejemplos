import csv

total = 0
contador = 0

# Solicitamos al usuario el nombre del fichero de salida y las columnas a leer
ficherosalida = input("Intruduce el nombre del fichero de salida): ")
sexo = input("Introduce el sexo a filtrar (Hombres/Mujeres): ")  
trimestre = input("Introduce el trimestre a filtrar (T1/T2/T3/T4): ")

# Abrimos el archivo CSV con la codificación adecuada: latin-1
with open('paro.csv','r', encoding='latin-1') as archivo_csv:
    # Creamos un lector CSV especificando el delimitador y el carácter de cita
    lector_csv = csv.reader(archivo_csv, delimiter=';', quotechar='"')
    with open(f"{ficherosalida}", "a") as salida:
      for fila in lector_csv:
        if fila[2] == sexo and trimestre in fila[3]:
           salida.write(f"Sexo : {fila[2]} Trimestre: {fila[3]} Paro: {fila[4]} \n")
           try:
             total = total + float(fila[4].replace(",", "."))
             contador = contador + 1
           except ValueError:
             print("Valor no numérico: ", fila[4])
print(f"Media del paro para sexo {sexo} en el trimestre {trimestre} es: {total/contador:.2f}%")
