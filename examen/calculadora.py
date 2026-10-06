continuar = "s"
salida = open("salida.txt","a")
# Usar las operaciones para que lo ponga en minuscula todo. 
while continuar == "s":
    operacion = input("¿Qué operación quieres realizar? (+ - * /): ")
    if operacion not in ("+","-","*","/"):
        print("Debes introuducir una operación válida: + - * /")
        continue
    try:	
        # si quitamos el int habrá un error a la hora de calcular. 
        n1 = int(input("ingresa el primer numero: "))
        n2 = int(input("ingresa el segundo numero: "))
    except ValueError:
        print("Ambos ")
    if operacion == "+":
        resultado = n1 + n2
        salida.write("La suma de {n1} + {n2} = {resultado}")
    elif operacion == "-":
        resultado = n1 - n2
        salida.write(f"La resta de {n1} - {n2} = {resultado}")
    elif operacion == "*":
        resultado = n1 * n2
        salida.write(f"La multiplicación de {n1} x {n2} = {resultado}")
    elif operacion == "/":
        try:
            salida.write(f"La división de {n1} / {n2} = {n1/n2}")
        except ZeroDivisionError:
            print("No se puede dividir por cero")
    # ¿Qué ocurre si el usuario pone SI en mayúsculas? Nada, está controlado
    continuar = input("¿Quieres continuar? s/n: ").lower()
