try:
    variable = float(input("Introduce el divisor: "))
    x = 1 / variable
except Exception as e:
    print(f"Ocurrió un error: {e}")
