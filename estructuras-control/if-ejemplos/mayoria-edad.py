# Definimos la variable edad
edad=int(input("Dime tu edad: "))

# Comparación 
if edad >= 18 and edad < 30:
	print("Eres mayor de edad, pero joven")
elif edad >= 30 and edad < 50:
	print("Eres mayor de edad, pero un poco viejo")
elif edad >=50:
	print("Eres ya un maduro") 
else:
	print("Puede ser que seas menor de edad o lo que has puesto es un error")

print("Fin del programa")
