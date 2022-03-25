# Ejercicio 6 - Ricardo Vaja
amigos = []
print("\nAgregue los nombres de los amigos que desea invitar para su cumpleaños, al finalizar escriba ´exit´.")
while input("\nPresione enter para continuar, de lo contrario, escriba ´exit´: \n") != "exit":
    amigos.append(input("Nombre: "))
print(*amigos, sep=" - ")
