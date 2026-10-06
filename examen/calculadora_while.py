continuar = "si"
resultado = 0
while continuar == "si":
	try:	
		print("Bienvenido a la calculadora en python!")
		n1 = int(input("ingresa el primer numero: "))
		n2 = int(input("ingresa el segundo numero: "))
		operacion = input("Operacion a realizar (+ - * /): ")

		if operacion == "+":
			resultado = n1 + n2
			print(f"La suma de {n1} + {n2} = {resultado}")
			continuar = input("Deseas continuar? si-no: ")

		elif operacion == "-":
			resultado = n1 - n2
			print(f"{n1} - {n2} = {resultado}")
			continuar = input("Deseas continuar? si-no: ")

		elif operacion == "*":
			resultado = n1 * n2
			print(f"{n1} x {n2} = {resultado}")
			continuar = input("Deseas continuar? si-no: ")

		elif operacion == "/":
			resultado = n1 / n2
			print(f"{n1} / {n2} = {resultado}")
			continuar = input("Deseas continuar? si-no: ")

		else:
			print("Debes poner una de las operaciones indicadas!")

		f=open("salida.txt","a")
		f.write(f"{n1} + {n2} = {resultado}\n")
		f.close()



	except ZeroDivisionError:
		print("No puedes dividir por 0!")
	except ValueError:
		print("Debes poner numeros!")
		n=open("errores.txt","a")
		n.write(f"Tipo de error en n1 o n2: {ValueError}\n")
		n.close()
	except:
		print("XD")
	
