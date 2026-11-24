import socket

HOST = "www.corellafp.es"
PORT = 80
# Vamos a crear una request mal construida para que el get de un error 400
request = (
    b"ESTO NO ES UNA PETICION HTTP\r\n"
    b"Host: www.corellafp.es\r\n"
    b"\r\n"
)

try:
    with socket.create_connection((HOST, PORT), timeout=5) as sock:
        sock.sendall(request)

        response = sock.recv(4096)

        print("Respuesta del servidor:")
        print(response.decode("utf-8", errors="replace"))

except socket.timeout:
    print("Timeout del servidor")

except OSError as e:
    print(f"Error: {e}")
