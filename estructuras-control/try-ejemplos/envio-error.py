# En este programa no analizamos un tipo concreto de posibles errores,
# tratamos cualquier error que se produzca y escribimos el mensaje de error en la variable error
# Inicializamos la variable al valor si, para que la condición del while sea verdadera.
continuar = "si"

# Comenzamos con el bucle 
while continuar == "si":
  try:
    # Estas sentencias se ejecutan siempre, pero están "protegidas" por el control de errores
    variable = float(input("Introduce el divisor: "))
    x = 1 / variable
    print("El resultado es: ", x)
  except Exception as error:
    # Esta sentencia solo se ejecuta si hay un error.
    print(f"Ocurrió un error, y el mensaje de error es el siguiente: {error}")
  finally:
    # Esta sentencia se ejecuta siempre, haya error o no lo haya. 
    continuar = input("Quieres continuar? ")
