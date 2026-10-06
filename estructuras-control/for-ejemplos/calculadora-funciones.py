# Funciones para las operaciones
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero no permitida"

# Función principal
def calculadora():
    print("Bienvenido a la calculadora")
    # While True es un blucle infinito de que podemo salir con break
    while True:
        # Menú de operaciones
        print("\nOperaciones disponibles:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        # Elección del usuario
        try:
            operacion = int(input("Selecciona la operación (1/2/3/4/5): "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue
        # Si el usuario elige salir utilizamos la sentencia break para salir del bucle infinito. 
        if operacion == 5:
            print("Gracias por usar la calculadora. ¡Hasta luego!")
            break

        if operacion in [1, 2, 3, 4]:
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
            except ValueError:
                print("Por favor, ingresa valores numéricos válidos.")
                continue

            # Realizar la operación seleccionada
            if operacion == 1:
                print(f"{num1} + {num2} = {sumar(num1, num2)}")
            elif operacion == 2:
                print(f"{num1} - {num2} = {restar(num1, num2)}")
            elif operacion == 3:
                print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
            elif operacion == 4:
                print(f"{num1} / {num2} = {dividir(num1, num2)}")
        else:
            print("Selección no válida, por favor elige una opción del 1 al 5.")

# Ejecutar la calculadora
calculadora()
