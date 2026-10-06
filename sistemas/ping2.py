import os
# Creamos una lista de direcciones
hosts = ["8.8.8.8", "google.com", "ldjslfkd","esteban.corellafp.es"]
# Recorremos la lista haciendo el ping
for host in hosts:
    # Definimos el comando enviado la respuesta del comando al /dev/null
    # Tambien enviamos los posibles errores al mismo "agujero".
    # Un error se puede producir por no haber red, no tener DNS o IP mal consttruida. 
    comando = f"ping -W 1 -c 1 {host} > /dev/null 2>&1"
    respuesta = os.system(comando)
    # La respuesta es 0 si el equipo está activo, 256 si no responde y 512 si hay un error
    f = open ("salida.txt","a") 
    if respuesta == 0:
        print(host, "ACTIVO")
        f.write(host, "está activo")
    elif respuesta == 256:
        print(host, "NO responde")
    elif respuesta == 512:
        #print("La respuesta es: ",respuesta)	
        print(host, "Error en la construcción de la ip o del DNS")
