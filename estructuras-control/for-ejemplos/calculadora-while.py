# Importamos el módulo OS que nos permite usar los comandos del Sistema Operativo 
import os
import time
# Pedimos los dos números decimales por pantalla

# Abrimos un while infinito 
while True:
  # Borramos la pantalla
  os.system('clear')
  # Pedimos la operación a realizar entre +-*/s
  operacion = input("\nintroduce la operación que quieres realizar: \nsuma (+)\nresta (-)\nmultiplicación (*)\ndivisión (/)\nsalir(s)\n: ")

  # Si la operación es salir nos despedimos y hacemos el break. 
  if operacion == "s":
    print("Hasta pronto")
    break

  # Si la operación es una aritmética pedimos los dos valores de los números. 
  if operacion in ["+", "-" , "*" ,"/"]:
    try:
       numero1 = float(input("introduce el numero 1: "))
       numero2 = float(input("introduce el numero 2: "))  
    except:
       print("Por favor, ingresa números validos")
       time.sleep(3)
       continue
  # Comenzamos a realizar las operaciones 
  if operacion == "+":  
    os.system('clear')
    print (f"\nEl resultado de sumar {numero1} + {numero2} es: {numero1+numero2:.2f}\n\n")
    time.sleep(3)
  elif operacion == "-":
    os.system('clear')
    print (f"\nEl resultado de restar {numero1} - {numero2} es: {numero1 - numero2:.2f}\n\n")
    time.sleep(3)
  elif operacion == "*":
    os.system('clear')
    print (f"\nEl resultado de multiplicar {numero1} x {numero2} es: {numero1 * numero2:.2f}\n\n")
    time.sleep(3)
  elif operacion == "/":
    os.system('clear')
    time.sleep(3)
    if numero2 != 0:
            print (f"\nEl resultado de dividir {numero1} / {numero2} es: {numero1/numero2:.2f}\n\n")
            time.sleep(3)
    else:
        print("\nNo se puede dividir por cero")
  else:
    print("Opción erronea")
