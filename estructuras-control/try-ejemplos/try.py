a = 3
b = 0
# Abrimos el control de excepciones y 
# metemos el el try la sentencia que puede dar error
try:
  print(a/b)
except:
  print("no se puede dividir por cero")

# Después del posible error el programa siguie normalmente.
print("El programa sigue ejecutandose normalmente")

# En cambio, si no controlamos las excepciones
# cuando se produce el error el programa se para y lanza un error
print(a/b)
print("Este print ya no se ejecuta")
