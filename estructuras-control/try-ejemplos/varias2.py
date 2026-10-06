try:
  numero1 = float(input("Introduce el primer numero: "))
  numero2 = float(input("Introduce el segundo numero: "))
  resultado = numero1/numero2
  print("El resultado es: ", resultado)
except:
  print("****************************")
  print("No se puede dividir por cero o debes poner un valor valido")
  print("****************************")
print("El programa continua normalmente")
