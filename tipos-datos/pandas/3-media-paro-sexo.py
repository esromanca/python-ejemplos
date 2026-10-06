import pandas as pd

# Leer el CSV
df = pd.read_csv("paro-completo.csv", encoding="latin-1", sep=";")

# Sustituir la coma por un punto
df["Total"] = df["Total"].str.replace(",", ".")

# Convertir la columna Total a numérica
df["Total"] = pd.to_numeric(df["Total"], errors="coerce")

media = df["Total"].mean()
print ("Esta es la media de la columna total: ", media)
# Pedir sexo al usuario
sexo_usuario = input("Introduce el sexo (por ejemplo: Hombres, Mujeres): ")

# Filtrar por el sexo introducido, en df_filtrado

df_filtrado = df[df["Sexo"] == sexo_usuario]

# Comprobar si hay datos con la función .empty
if df_filtrado.empty:
    print("No hay datos para ese sexo.")
else:
    # Calcular la media
    media = df_filtrado["Total"].mean()
    moda = df_filtrado["Total"].mode()
    estadisticas = df_filtrado["Total"].agg(["mean","median", "min", "max"])
    print(f"La media de paro para el sexo '{sexo_usuario}' es: {media:.2f} y la moda es: {moda}")
    print(estadisticas)
