import pandas as pd

midf = pd.read_csv("paro-completo.csv", encoding="iso-8859-1",sep=";")

#print(midf)
midf["Total"] = midf["Total"].str.replace(",", ".")
#midf["Total"] = pd.to_numeric(midf["Total"], errors="coerce")
midf["Total"] = pd.to_numeric(midf["Total"])

media = midf["Total"].mean()

print(f"La media es: {media:.2f}")
