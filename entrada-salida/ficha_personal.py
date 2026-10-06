# declaración de variables y inicialización de sus valores
id_usuario = 412
nombre = "Carlos Mendoza"
edad = 34
progreso_capacitacion = 0.875
salario_anual = 45800.50
eficiencia = 1450000.953

# Corrección del formato 
salario_es = f"{salario_anual:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

# Cuando multiplicamos un texto como "=" por un número, repite el texto tantas veces como el número. 
print("=" * 45)

# El acento circunflejo del 45 siginifica "centrar" en un espacio de 45.
print(f"{'FICHA DE EMPLEADO':^45}")
print("=" * 45)

# El | es un adorno y el menor es para que justifique a la izquierda y reserve un campo de 20 espacios. 
print(f"Empleado ID: {id_usuario:06d} | Nombre: {nombre:<20}")
print(f"Edad: {edad} años")
print("-" * 45)
print(f"{'Métrica':<25} | {'Valor':>15}")
print("-" * 45)
print(f"{'Progreso de Curso':<25} | {progreso_capacitacion:>15.1%}")
print(f"{'Salario Anual':<25} | {salario_es:>15}")
print(f"{'Operaciones Procesadas':<25} | {eficiencia:>15.2e}")
print("=" * 45)
