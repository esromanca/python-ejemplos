try:
  numero1 = float(input("Introduce el primer numero: "))
  numero2 = float(input("Introduce el segundo numero: "))
  resultado = numero1/numero2
  print("El resultado es: ", resultado)
except ZeroDivisionError:
  print("****************************")
  print("No se puede dividir por cero")
  print("****************************")
except ValueError:
  print("********************************")
  print("Debes introducir numeros validos")
  print("********************************")
except:
  print("except")
print("El programa continua normalmente")
