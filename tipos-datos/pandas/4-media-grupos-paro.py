# Importamos la librería PANDAS y creamos un alias de la librería.
import pandas as pd
# Creamos un objeto PANDAS a partir de un fichero CSV, codificado con latin-1, con separdor ; y saltando las líneas corruptas.
mipandaCSV = pd.read_csv("paro-completo.csv",encoding="iso-8859-1", sep=";", on_bad_lines="skip")
# Tratamos el contenido para convertir Total en un valor númérico válido
mipandaCSV["Total"] = mipandaCSV["Total"].str.replace(",", ".")
# Transformamos el contenido de Total en valores numéricos
# Si algún valor no se puede transformar se sustituye por NaN, que no se tiene en cuenta en los calculos. 
mipandaCSV["Total"] = pd.to_numeric(mipandaCSV["Total"], errors="coerce")
# Agrupar por el valor de una columna (por ejemplo 'Sexo')
# grupoSexo = mipandaCSV.groupby("Sexo")
# Agrupar los registros por el valor de dos columnas, el orden es importante. 
grupos = mipandaCSV.groupby(["Comunidades","Sexo"])

# Calcular estadísticas de la columna "Total" dentro de los grupos creados. 
estadisticas = grupos["Total"].agg(['mean', 'sum', 'count', 'min', 'max'])
print(estadisticas.to_string())
#print(estadisticas) de esta forma estaba truncando y mostraba ... en lugar de el valor
#print(grupoSexo)
