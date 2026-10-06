import pandas as pd

# Leer el CSV
df = pd.read_csv("paro-completo.csv", encoding="latin-1", sep=";")

# Convertir Total a numérico
df["Total"] = df["Total"].str.replace(",", ".")
df["Total"] = pd.to_numeric(df["Total"], errors="coerce")

while True:
    print("\nMENÚ")
    print("1. Mostrar la media total de paro")
    print("2. Mostrar la media de paro por sexo")
    print("3. Filtrar datos por comunidad")
    print("4. Mostrar la media de paro por periodo")
    print("5. Exportar a CSV la media por comunidades")
    print("0. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        # Hacemos la media usando la columna Total
        media_total = df["Total"].mean()
        print(f"La media total de paro es: {media_total:.2f}")

    elif opcion == "2":
        # hacemos grupos por "sexo" () y calculamos la media con Total []
        # Cuando hacemos un groupby, no creamos un DF normal, creamos un Objeto GroupBy que debemos recorrer. 
        medias_sexo = df.groupby("Sexo")["Total"].mean()
        print("\nMedia de paro por sexo:")
        print(medias_sexo.round(2))

    elif opcion == "3":
        comunidad = input("Introduce una comunidad: ").strip()
        filtrado = df[df["Comunidades"].str.contains(comunidad, case=False, na=False)]
        # Si queremos solo los nombres distintos de filtrado podemos usar
        print(filtrado["Comunidades"].unique())
        if filtrado.empty:
            print("No hay datos para esa comunidad.")
        else:
            media = filtrado["Total"].mean()
            print(f"\nDatos de la comunidad {comunidad} es:{media:.2f}")
            print(media)

    elif opcion == "4":
        # Añadimos una columna más al DataFrame, de esta forma podemos agrupar por trimestres. 
        df["Trimestre"] = df["Periodo"].str.extract(r"(T\d)")
        medias_periodo = df.groupby("Trimestre")["Total"].mean()
        print("\nMedia de paro por trimestre:")
        print(medias_periodo.round(2))

    elif opcion == "5":
        medias_comunidades = df.groupby("Comunidades")["Total"].mean().round(2)
        medias_comunidades.to_csv("media_por_comunidades.csv")
        print("Archivo 'media_por_comunidades.csv' creado correctamente.")
        print("Media del paro por comunidades")
        print(medias_comunidades)
    elif opcion == "0":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")
