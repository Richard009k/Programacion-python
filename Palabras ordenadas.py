palabras= []

def ingresar_palabras():
    try:
        palabras.append(input("Ingrese palabras: "))
        print(sorted(palabras))  
    except:
        print("Solo se admiten palabras")
while True:
    ingresar_palabras()