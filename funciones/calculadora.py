# Funciones para cada operación

def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    # Controlamos división entre cero
    if b == 0:
        return "Error: No se puede dividir entre cero"
    return a / b


# Programa principal

def calculadora():

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
        resultado = sumar(num1, num2)

    elif opcion == "2":
        resultado = restar(num1, num2)

    elif opcion == "3":
        resultado = multiplicar(num1, num2)

    elif opcion == "4":
        resultado = dividir(num1, num2)

    else:
        resultado = "Opción no válida"

    # Mostrar resultado
    print("\nResultado:", resultado)


# Ejecutar programa
calculadora()
