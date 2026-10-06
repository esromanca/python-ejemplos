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


