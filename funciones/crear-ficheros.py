import os
def crea_ficheros(ruta, nombre, cantidad):
    if not os.path.exists(ruta):
        os.makedirs(ruta)
    for i in range(cantidad):
        archivo_ruta = os.path.join(ruta, f"{nombre}_{i}.txt")
        with open(archivo_ruta, 'w') as fichero:
            fichero.write(f'hola mundo: fichero {i}')
        print(f"Creado: {archivo_ruta}")

crea_ficheros("./ejemplo", "fichero", 10)
