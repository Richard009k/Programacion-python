# Ejercicio 9 - Ricardo Vaja
numero1= 0
numero2= 0
resultado= 0
operacion= ""

operacion= input("que operacion desea realizar? ingrese el simbolo: ")
numero1= float(input("Ingrese un numero: "))
numero2= float(input("Ingrese otro numero: "))

if operacion == "+" :
    resultado= (numero1+numero2)
elif operacion == "-" :
    resultado= (numero1-numero2)
elif operacion == "*":
    resultado= (numero1*numero2)
elif operacion == "/":
    resultado = (numero1/numero2)
print(f"{numero1} {operacion} {numero2} es igual a {resultado}")