a = float(input("Escribe el primer número: "))
b = float(input("Escribe el segundo número: "))
if b > a:
  print(f"El valro {b} es mayor que el valor {a}")
elif a == b:
  print(f"El valro {a} es mayor que el valor {b}")
# La sentencia else captura cualquier cosa que hayan capturado las anteriores. 
else:
  print("Supongo que A es mayor que B")
