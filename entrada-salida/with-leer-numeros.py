# Instrucciones fuera del bucle with
print("Inicio del programa")

with open ("numeros.txt","r", encoding="utf-8") as numeros:
   # Instrucciones dentrode with, en las que el fichero está abierto
   contenido = numeros.read()
   print (contenido)
   for i in contenido:
      print(i)
   # ¿Dónde está ahora posicionado el puntero de lectura
   # cuando ejecutamos read(), Python lee todo el contenido del fichero y deja el puntero de lectura al final del fichero (EOF).
   numeros.seek(0)
   linea = numeros.readline()
   while linea != "":
      print(linea, end="")
      linea = numeros.readline()

# Instrucciones fuera del with, el fichero ya está cerrado. 
print("El fichero ya está cerrado")
print("Fin del programa")
