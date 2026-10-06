import pandas as pd

# Leer el CSV y meter la información en un DataFrame llamado df
midf = pd.read_csv("paro-completo.csv", encoding="latin-1", sep=";")

print(midf)
# Sustituir la coma por un punto de la columna llamada Total
midf["Total"] = midf["Total"].str.replace(",", ".")

# Convertir la columna Total a numérica
midf["Total"] = pd.to_numeric(midf["Total"], errors="coerce")

# Calcular la media de la columna llamada Total
media = midf["Total"].mean()

#Imprimir en pantalla la media de la columna Total
print(f"La media de paro es: {media:.2f}")
