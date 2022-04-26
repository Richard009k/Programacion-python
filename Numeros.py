numeros = []
def ingresar_numeros():
    try:
        numeros.append(int(input("Ingrese un numero: ")))
        sum_lista=sum(numeros)
        promedio=(sum_lista / len(numeros))
        numero_menor=min(numeros)
        numero_mayor= max(numeros)
        print(f"El numero mayor es {numero_mayor}")
        print(f"El numero menor es {numero_menor}")
        print(f"El total es {sum_lista}")
        print(f"El promedio es {promedio}")
    except:
        print("Solo se admiten numeros")
while True:
    ingresar_numeros()