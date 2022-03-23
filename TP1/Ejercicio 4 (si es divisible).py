numero1= int(input("Ingrese un numero entero: "))
numero2= int(input("Ingrese otro numero entero: "))
operacion= 0
operacion= numero1 % numero2
if operacion == 0:
    print(f"{numero1} es divisible por {numero2}")
else:
    print(f"{numero1} no es divisible por {numero2}")