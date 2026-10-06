# Abrimos el fichero de entrada de datos 
f = open("numeros.txt")

# Leemos las tres primeras líneas y asignamos los valores a las tres variables 
n1 = int(f.readline())
n2 = int(f.readline())
n3 = int(f.readline())

# Calculamos el resultado, lo imprimimos en pantalla y cerramos el fichero. 
resultado = n1 + n2 + n3
print(f"La suma de {n1} + {n2} + {n3} es {resultado}")
f.close()

# Abrimos un fichero nuevo para escribir el resulado. 
fsalida = open("salida.txt","x")
fsalida.write(f"la suma de {n1} + {n2} + {n3} es {resultado}\n")
fsalida.close()
