# Importamos la librería csv para manejar archivos CSV
import csv

# Inicializamos las variables para calcular la media
total = 0
contador = 0

# Solicitamos los datos al usuario
nombre = input("Introduce el nombre del fichero de salida: ")
sexo = input("Introduce el sexo a filtrar (Hombres/Mujeres): ")
trimestre = input("Introduce el trimestre a filtrar (T1/T2/T3/T4): ")

# Abrimos el archivo CSV
with open('paro.csv', 'r', encoding='latin-1') as archivo_csv:

    # Creamos el lector CSV
    lector_csv = csv.reader(archivo_csv, delimiter=';', quotechar='"')

    # Guardamos la primera línea como encabezado
    encabezado = next(lector_csv)

    # Abrimos el fichero de salida
    with open(nombre, 'a', encoding='latin-1') as f:

        # Recorremos todas las filas del CSV
        for fila in lector_csv:

            # Filtramos por sexo y trimestre
            if fila[2] == sexo and trimestre in fila[3]:

                try:
                    # Intentamos convertir el valor a número
                    valor = float(fila[4].replace(',', '.'))

                except ValueError:
                    # Si no es numérico, mostramos un mensaje
                    print("Valor inválido de paro:", fila[4])

                    # Saltamos a la siguiente fila
                    continue

                # Si es numérico, escribimos el registro
                f.write(
                    f"Sexo: {fila[2]} Trimestre: {fila[3]} "
                    f"Paro: {fila[4]}\n"
                )

                # Acumulamos el valor y aumentamos el contador
                total += valor
                contador += 1

# Calculamos e imprimimos la media
if contador > 0:
    media = total / contador

    print(
        f"Media del paro para sexo {sexo} "
        f"en el trimestre {trimestre} es: {media:.2f}%"
    )

else:
    print("No hay valores numéricos para calcular la media.")
