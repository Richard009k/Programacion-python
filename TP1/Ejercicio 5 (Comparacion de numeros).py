numero1 = float(input("Inserte un numero: "))
numero2 = float(input("Inserte un numero: "))
numero3 = float(input("Inserte un numero: "))
if (numero1 > numero2 and numero1 > numero3):
    print(f"\n{numero1} es mas grande")
elif numero2 > numero1 and numero2 > numero3:
    print(f"\n{numero2} es mas grande")
elif numero3 > numero1 and numero3 > numero2:
    print(f"\n{numero3} es mas grande")