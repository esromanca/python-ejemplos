import pandas as pd

# 1. Leer el fichero CSV
# Pandas se encarga de abrir el fichero y de crear la estructura de datos en un paso 
# datos.csv tiene dos campos: categoría y valor
df = pd.read_csv("paro-completo.csv",encoding="latin-1",sep=";")

df["Total"] = df["Total"].str.replace(",", ".")
# Transformamos el contenido de Total en valores numéricos
# Si algún valor no se puede transformar se sustituye por NaN, que no se tiene en cuenta en los calculos. 
df["Total"] = pd.to_numeric(df["Total"], errors="coerce")

# 2. Agrupar por una columna (por ejemplo 'categoria')
grupo = df.groupby(["Sexo","Comunidades"])

# 3. Calcular estadísticas
estadisticas = grupo["Total"].agg(['mean', 'sum', 'count', 'min', 'max'])

print(estadisticas)

fichero = open("salida.txt","w")
fichero.write(estadisticas.to_string())
fichero.close()
