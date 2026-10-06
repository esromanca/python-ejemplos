# En este caso controlamos todas las excepciones que se producen, por lo que parece que el finally no es importante 
resultado = None
continuar = "si"
fichero = None
while continuar == "si" or continuar == "sí" or continuar == "Si":
  try:
    fichero = open("fichero.txt","r")
    # ¿Qué ocurre si nos olvidamos de poner un paréntesis, sería una excepción que no controlamos
    numero1 = float(input("escribe el divisor: "))
    resultado = 1 / numero1
  #except ValueError:
  #  print("Tienes que introducir un número")
  except ZeroDivisionError:
    print("No se puede dividir por cero")
  except FileNotFoundError: 
    print("El fichero no exixte, por favor crealo")
  finally:
    if fichero is not None:
       fichero.close()
       print("Estoy en el Finally")
  continuar = input("quieres continuar?")

fichero.close()
print("\n*****************************************")
print("El resultado de la operación es: ",resultado)
print("*****************************************")

# Aquí se produce una excepción no controlada, por lo que el programa finalizaría abruptamente
# En este caso el finally es fundamental para que se liberen los recursos necesarios. 
