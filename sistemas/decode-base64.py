import base64

credenciales1 = input("introduce el código en base64 para descodificar: ")
#credenciales = "dXN1MTpJZXNBbmdlbENvcmVsbGExMjNA"

#print(base64.b64decode(credenciales).decode())
print(base64.b64decode(credenciales1).decode())
