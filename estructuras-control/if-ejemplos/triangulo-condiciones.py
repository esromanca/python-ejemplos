print("Introduzca la longitud de los tres lados de un triángulo: ")
lado1 = int(input("Lado 1: "))
lado2 = int(input("Lado 2: "))
lado3 = int(input("Lado 3: "))
if (lado1 == lado2 and lado2 == lado3):
   print("Es un triángulo equilátero.")
elif (lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
   print("Es un triángulo isósceles.")
else:
   print("Es un triángulo escaleno.")
