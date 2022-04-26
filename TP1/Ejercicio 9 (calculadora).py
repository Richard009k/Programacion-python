# Ejercicio 9 - Ricardo Vaja
numero1= 0
numero2= 0
resultado= 0
operacion= ""
n_valido= False

operacion= input("que operacion desea realizar? ingrese el simbolo: ")
while n_valido == False:
    numero1= float(input("Ingrese un numero: "))
    if not numero1.isdigit():
    print("Solo se pueden ingresar numeros")
    else:
        n_valido = True
        
numero2= float(input("Ingrese otro numero: "))
if numero2.isdigit():
    print("Solo se pueden ingresar numeros")

if operacion == "+" :
    resultado= (numero1+numero2)
elif operacion == "-" :
    resultado= (numero1-numero2)
elif operacion == "*":
    resultado= (numero1*numero2)
elif operacion == "/":
    resultado = (numero1/numero2)
print(f"{numero1} {operacion} {numero2} es igual a {resultado}")