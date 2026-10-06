# Este programa lee de un fichero con una columna de números
# En cada fila hay un número, y suma de tres en tres. 
# Pide el nombre del fichero de salida donde escribirá  los resultados de las tres sumas
# Después escribe el restulado de la suma de los 9 números en el fichero inicial de numeros.txt 

# Nivel 1
with open("numeros.txt","r") as numeros:
    n1 = float(numeros.readline())
    n2 = float(numeros.readline())
    n3 = float(numeros.readline())
    print(n1+n2+n3)

    n4 = float(numeros.readline())
    n5 = float(numeros.readline())
    n6 = float(numeros.readline())
    print(n4+n5+n6)

    n7 = float(numeros.readline())
    n8 = float(numeros.readline())
    n9 = float(numeros.readline())
    print(n7+n8+n9)

# Pedimos el nombre de salida, lo abrimos y escribimos las sumas parciales de los grupos de tres números. 
nombre = input("Escribe el nombre del fichero de salida: ")
fichero = open(f"{nombre}","w")
fichero.write(f"la suma es {n1+n2+n3}\n")
with open(f"{nombre}","w") as s:
    s.write(f'La suma de los tres primeros númers es: {n1+n2+n3:.2f}\n')
    s.write(f'La suma de los tres primeros númers es: {n4+n5+n6:.2f}\n')
    s.write(f'La suma de los tres primeros númers es: {n7+n8+n9:.2f}\n')
# Nivel 2
# Ahora escribimos el resultado completo en el fichero de origen números
with open("numeros.txt","a+") as numeros:
    numeros.write(f'la suma de todos es: {n1+n2+n3+n4+n5+n6+n7+n8+n9:-2f}\n')

# Nivel 3
# Ahora vamos a crear un nuevo fichero y a copiar toda la información de los ficheros anteriores. 
with open("fichero-completo.txt","w") as completo:
       with open("numeros.txt", "r") as numeros:
           completo.write(numeros.read())
       with open(f"{nombre}","r") as salida:
           completo.write(salida.read())
