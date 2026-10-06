# Imortamos la librería csv para manejar archivos CSV
import csv
total = 0
contador = 0
# Solicitamos al usuario el nombre del fichero de salida y las columnas a leer
nombre = input("Intruduce el nombre del fichero de salida): ")
sexo = input("Introduce el sexo a filtrar (Hombres/Mujeres): ")  
#columna1 = int(input("Introduce la columna1 a leer (1-5): "))
#columna2 = int(input("Introduce la columna2 a leer (1-5): "))
trimestre = input("Introduce el trimestre a filtrar (T1/T2/T3/T4): ")
#edad = input("Introduce la edad a filtrar (0-100/Todos): ")
# Abrimos el archivo CSV con la codificación adecuada: latin-1
with open('paro.csv','r', encoding='latin-1') as archivo_csv:
    # Creamos un lector CSV especificando el delimitador y el carácter de cita
    lector_csv = csv.reader(archivo_csv, delimiter=';', quotechar='"')
    # Guardamos la primera linea como encabezado. 
    encabezado = next(lector_csv)
    # Abrimos el fichero de salida en modo append dentro del with anterior 
    # para poder usar lector_csv. en caso contrario se cerraría. 
    with open(f"{nombre}", "a") as f:
      f.write(encabezado[2] + " " + encabezado[3] + " " + encabezado[4] + "\n")
      for fila in lector_csv:
        # Escribimos los datos en el fichero de salida
        print("Valor fila 3", fila[3], "Valor de TRIMESTRE: ", trimestre)  
        if fila[2] == sexo and trimestre in fila[3]:
           f.write(f"Sexo : {fila[2]} Trimestre: {fila[3]} Paro: {fila[4]} \n")
           total = total + float(fila[4].replace(",", "."))
           contador += 1 
print(f"Media del paro para sexo {sexo} en el trimestre {trimestre} es: {total/contador:.2f}%")
