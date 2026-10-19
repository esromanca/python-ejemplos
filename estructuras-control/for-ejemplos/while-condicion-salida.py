variable = "si"
i = 0
while variable.lower() in ("si","sí","yes"):
   print("Estoy dentro del while")
   i = i + 1
   print(f"se ha repetido {i} veces")
   variable = input("Quieres continuar? ")
