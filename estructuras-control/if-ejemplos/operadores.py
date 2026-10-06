x=2; y=3
print("Operadores Relacionales")
print("x==y =", x==y) # Se imprimirá el resultado de la condición FALSE en este caso
print("x!=y =", x!=y) # True
print("x>y  =", x>y)  # False
print("x<y  =", x<y)  # True
print("x>=y =", x>=y) # False
print("x<=y =", x<=y) # True
print("a es hola: ", "a" is "hola")
print("a está en hola: ", "a" in "hola")

cadena = "hola"
subcadena ="a"
if subcadena in cadena:
	print("a esta en hola")
else:
	print("a no está en hola")

cadena_principal = "Hola mundo, este es un ejemplo."
subcadena = "mundo"

if cadena_principal.find(subcadena) != -1:
  print(f"'{subcadena}' se encuentra en la posición: {cadena_principal.find(subcadena)}")
else:
  print(f"'{subcadena}' NO se encuentra en la cadena.")
