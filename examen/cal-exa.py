# Ejecicio del examen de Python de Sistemas Microinformáticos y Redes.
continuar = "s"
salida = open("salida.txt","w")
while continuar == "s":
    operacion = input("¿Qué operación quieres realizar? (+ - * /): ")
    if operacion not in ("+","-","*","/"):
        print("Debes introuducir una operación válida: + - * /")
        continue
    try:
        n1 = float(input("ingresa el primer numero: "))
        n2 = float(input("ingresa el segundo numero: "))
    except ValueError:
        print("Debes introducir números")
    if operacion == "+":
        salida.write(f"La suma de {n1} + {n2} = {n1+n2}")
    elif operacion == "-":
        resultado = n1 - n2
        salida.write(f"La resta de {n1} - {n2} = {n1-n2}")
    elif operacion == "*":
        resultado = n1 * n2
        salida.write(f"La multiplicación de {n1} x {n2} = {n1*n2}")
    elif operacion == "/":
        try:
            salida.write(f"La división de {n1} / {n2} = {n1/n2}")
        except ZeroDivisionError:
            print("No se puede dividir por cero")
    continuar = input("¿Quieres continuar? s/n: ").lower()
