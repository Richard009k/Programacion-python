from ast import Break
import random
puntos= 0

while True:
    if puntos == 3:
        break
    try: 
        print("1) Piedra")
        print("2) Papel")
        print("3) Tijera")
        opcion = int(input("Elije una opcion: \n"))
        pc= random.randrange(1,3)
    
        if opcion == 1:
            usuario_elije = "Piedra"
        elif opcion == 2:
            usuario_elije = "Papel"
        elif opcion == 3:
            usuario_elije == "Tijera"
        print (f"\nElejiste: {usuario_elije}")
    

        if pc == 1:
            cpu = "Piedra"
        elif pc == 2:
            cpu = "Papel"
        elif pc == 3:
            cpu == "Tijera"
        print (f"CPU eligio: {cpu}")

        if pc == opcion: #empate
            print("Empate\n")
        elif pc == 1 and opcion == 2: #pc piedra/papel
            print("Ganaste, Papel envuelve piedra\n")
            puntos +=1
        elif pc == 1 and opcion == 3: #pc piedra/Tijera
            print("Perdiste, Piedra rompe tijera\n")
        elif pc == 2 and opcion == 1: #pc papel/ piedra
            print("Perdiste, Papel envuelve piedra\n")
        elif pc == 2 and opcion == 3: #pc Papel/ Tijera
            print("Ganaste, Tijera corta papel\n")
            puntos +=1
        elif pc == 3 and opcion == 1: #pc tijera/Piedra
            print("Ganaste, Piedra rompe tijera")
            puntos +=1
        elif pc == 3 and opcion == 2: #pc tijera/papel
            print("Perdiste, Tijera corta papel\n")
    except:
        print("\nSolo se pueden ingresar los numeros 1, 2 o 3\n")

        
