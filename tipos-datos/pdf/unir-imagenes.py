from PIL import Image

rutas = ["pagina1.jpeg", "pagina2.jpeg", "pagina3.jpeg"]
salida = "unido.pdf"

# Abrimos las imágenes y las convertimos a RGB (requisito para exportar a PDF)
imagenes = [Image.open(ruta).convert("RGB") for ruta in rutas]

# Guardamos la primera y añadimos el resto como páginas siguientes
imagenes[0].save(salida, save_all=True, append_images=imagenes[1:])
