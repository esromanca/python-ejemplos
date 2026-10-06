import subprocess

hosts = ["192.168.1.1", "192.168.1.10", "8.8.8.8", "192.168.1.50"]

for host in hosts:
    resultado = subprocess.run(
        ["ping", "-c", "1", host],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    
    if resultado.returncode == 0:
        print(f"{host} ACTIVO")
    else:
        print(f"{host} NO responde")
