with open ("numeros.txt","r") as numeros:
   contenido = numeros.read()
   for i in contenido:
      print(i)
