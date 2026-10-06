import pandas as pd

# 1. Leer el fichero CSV
# Pandas se encarga de abrir el fichero y de crear la estructura de datos en un paso 
# datos.csv tiene dos campos: categoría y valor
# datos.csv está codificado en UTF-8 y separado por comas (son los valores por defecto)
midf = pd.read_csv("1-datos.csv")
media = midf["valor"].mean()
print(f"La media del campo valor es: {media}")
maximo = midf["valor"].max()
print(f"El sueldo máximo es: {maximo}")
minimo = midf["valor"].min()
print(f"El sueldo mínimo es: {minimo}")
# 2. Agrupar por una columna (por ejemplo 'categoria')
#grupos = midf.groupby(["categoria"])

# 3. Calcular estadísticas
#estadisticas = grupos["valor"].agg(['mean', 'sum', 'count', 'min', 'max'])
#estadisticas = grupos["valor"].mean()
estadisticas = midf.groupby("sexo")["valor"].agg(["mean", "min", "max"])
print(estadisticas)
