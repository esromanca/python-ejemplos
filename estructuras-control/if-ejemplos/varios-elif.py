# Primero solicitamos un número. 
a = float(input("Escribe el primer número: "))

# Se comprueba la primera condición, si la cumple ejecuta el bloque, si no pasa a la siguiente
# Este caso puede ser confuso ya que el primer elif incluye al primero, pero no hay problema
# Ya que nunca llegaría al elif si el numero está por debajo de 10
if a < 10:
  print("el número es menor de 10")
elif a < 20:
  print("El número está entre 10 y 19")
# La sentencia else captura cualquier cosa que hayan capturado las anteriores. 
elif a < 30:
  print("el número esta entre 20 y 29")
else:
  print("El número es 30 o más")
