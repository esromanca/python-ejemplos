import csv
# La codificación 'ISO 8859-1' es común en archivos CSV en español
# Para incluir caracteres especiales como tildes y eñes. 
# Por defecto, Python usa 'utf-8' que puede no manejar estos caracteres correctamente.
with open('paro.csv' , newline='', encoding='ISO 8859-1') as fichero:
    # newline='' es importante para evitar problemas con las nuevas líneas en diferentes sistemas operativos
    csvlectura = csv.reader(fichero, delimiter=';', quotechar='"')
    print(type(csvlectura))
    # Si no especificamos delimiter y quotechar, csv.reader usará los valores por defecto (coma y comillas dobles)
    # reader es un objeto iterable que produce cada fila del archivo como una lista de cadenas
    for fila in csvlectura:
        #print(fila)
        #print("sexo: ",fila[2],"-----", "paro calculado : ",fila[4])  # Acceder a elementos específicos por índice 
        print(f"Comunidad: {fila[0]} --- Edad: {fila[1]} --- sexo: {fila[2]} ---- Paro calculado: {fila[4]}")  # Acceder a elementos específicos por índice 
