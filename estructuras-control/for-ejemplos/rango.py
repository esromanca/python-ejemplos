# La variable i tomará los primeros 5 valores comenzando por el cero. 
# El rango puede tener tres parámetros: limite superior, inicio y salto.
# Solo un valor, la variable i comienza en 0 y termina en 9
print("=" * 45)
print(f"{'UN SOLO PARÁMETRO: range(fin)':^45}")
print("=" * 45)
for i in range(10):
    print("el valor de i es: ", i)

# Dos valores
print("=" * 45)
print(f"{'DOS PARÁMETROS: rangue(inicio,fin)':^45}")
print("=" * 45)
for i in range(3,10):
     print("el valor de i es: ", i)

# Tres valores
print("=" * 45)
print(f"{'TRES PARÁMETROS: rangue(inicio,fin,salto':^45}")
print("=" * 45)
for i in range(3,10,2):
    print("el valor de i es: ", i)
#    for j in range(3):
#         print(f"    el valor de i es: {i} y el valor de j es: {j}")
