# Ejercicio 10 - Ricardo Vaja
import random
numero = random.randint(0, 10)
intentos = 5
otravez= ""
while intentos != 0:
    adivina= int(input(f"Adivine el numero, {intentos} intentos: \n"))
    if adivina > numero:
        print(f"El numero es mas chico que {adivina}\n")
        intentos -=1
    elif adivina < numero:
        print(f"El numero es mas grande que {adivina}\n")
        intentos -=1
    elif adivina == numero:
        print(f"Has adivinado!!! el numero era {adivina}\n")
        otravez= input("Queres intentarlo otra vez? si/no: \n")
        if otravez == "si":
            intentos = 5
        else:
            print("Fin de la partida.")
    if intentos == 0:
        print(f"Perdiste!!! El numero era {numero}\n")
        otravez= input("Queres intentarlo otra vez? si/no: \n")
        if otravez == "si":
            intentos = 5
        else:
            print("Fin de la partida.")
     



