# Funciones para cada operación
import operaciones

# Programa principal

print("=== CALCULADORA ===")

    # Pedir números
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

    # Pedir operación
print("\nElige una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("Introduce una opción (1/2/3/4): ")

    # Elegir operación
if opcion == "1":
   resultado = operaciones.sumar(num1, num2)

elif opcion == "2":
   resultado = operaciones.restar(num1, num2)

elif opcion == "3":
   resultado = operaciones.multiplicar(num1, num2)

elif opcion == "4":
   resultado = operaciones.dividir(num1, num2)

else:
   resultado = "Opción no válida"

    # Mostrar resultado
print("\nResultado:", resultado)
