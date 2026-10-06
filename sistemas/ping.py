import os
# Creamos una lista de direcciones
hosts = ["8.8.8.8", "google.com", "ldjslfkd","esteban.corellafp.es"]
# Recorremos la lista haciendo el ping
for host in hosts:
    # Definimos el comando enviado la respuesta del comando al /dev/null
    # Tambien enviamos los posibles errores al mismo "agujero".
    # Un error se puede producir por no haber red, no tener DNS o IP mal consttruida. 
    comando = f"ping -W 2 -c 1 {host} > /dev/null 2>&1"
    respuesta = os.system(comando)
    # La respuesta es 0 si el equipo está activo, 256 si no responde y 512 si hay un error
    if respuesta == 0:
        print(host, "ACTIVO")
    else:
        print(host, "NO responde")
        print("La respuesta es: ",respuesta)	
