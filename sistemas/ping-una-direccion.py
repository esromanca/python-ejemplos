import os

ip = "127.0.0.1"  # Cambia esta IP a la que necesites verificar

# Ejecuta el comando ping ('-c 1' para 1 intento, compatible con Linux/macOS)
# Para Windows usaríamos '-n 1' en lugar de '-c 1'
# Si no sabes qué sistema operativo estás usando puedes hacer una comprobación:
import sys
print(sys.platform)
if sys.platform == "win32":
    ping_command = f"ping -n 1 {ip}"
else:
    ping_command = f"ping -c 1 {ip}"
print(ping_command)
respuesta = os.system(ping_command)

if respuesta == 0:
    print(f"La IP {ip} está activa.")
else:
    print(f"La IP {ip} no responde.")
