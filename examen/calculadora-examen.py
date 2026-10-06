# Ejecicio del examen de Python de Sistemas Microinformáticos y Redes. 
continuar = "s"
salida = open("salida.txt","r")
while continuar == "s":
    operacion = input("¿Qué operación quieres realizar? (+ - * /): ")
    if operacion not in ("+","-","*","/")
        print("Debes introuducir una operación válida: + - * /")
        continue
    try:
        n1 = input("ingresa el primer numero: ")
        n2 = input("ingresa el segundo numero: ")
    except ValueError:
        print("Debes introducir números")
    if operacion == "+":
        salida.write("La suma de {n1} + {n2} = {n1+n2}")
    elif operacion == "-":
        resultado = n1 - n2
        salida.write("La resta de {n1} - {n2} = {n1-n2}")
    elif operacion == "*":
        resultado = n1 * n2
        salida.write("La multiplicación de {n1} x {n2} = {n1*n2}")
    elif operacion == "/":
        try:
            salida.write("La división de {n1} / {n2} = {n1/n2}")
        except ZeroDivisionError:
            print("No se puede dividir por cero")
    continuar = input("¿Quieres continuar? s/n: ").lower()
