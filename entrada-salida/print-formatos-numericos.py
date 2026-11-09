# Limitar el número de decimales. 
pi = 3.14159
# pasar un porcentaje en tanto por uno a uno en tanto por 100 y añadir el simbolo. 
porcentaje = 0.8556
# Poner los simbolos separando los miles. 
gran_numero = 1000000
# Completar poniendo ceros a la izquierda hasta cierto tamaño. 
entero = 42

# Decimales
print(f"Pi con dos decimales: {pi:.2f}")  # Output: 3.14

# Porcentaje
print(f"Progreso: {porcentaje:.1%}")      # Output: 85.6%

# Separador de miles
print(f"Saldo: ${gran_numero:,}")         # Output: $1,000,000

# Relleno de ceros (para códigos o IDs)
print(f"ID de usuario: {entero:06d}")     # Output: 000042
