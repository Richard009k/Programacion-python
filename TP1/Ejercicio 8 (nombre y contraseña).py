# Ejercicio 8 - Ricardo Vaja

datos_usuario= []
contraseña= ""
caracteres_esp= ["!","#","@","$","%","&"]
vocales= ["a","e","i","o","u"]
contador=0
validar_contra= False
validar_nombres=False
validar_año=False


#datos_usuario.append(input("\nIngrese el año de nacimiento: \n"))
#contraseña= input("Ingrese una contraseña")


while validar_nombres==False:
    datos_usuario.insert(0,input("\nIngrese su apellido: \n"))
    datos_usuario.insert(1,input("\nIngrese su nombre: \n"))
    for vocal in vocales: 
        for letras in datos_usuario[0] + datos_usuario[1]: 
            if vocal == letras:
                contador+=1
            
    if contador <= 3:
        print("Debe tener al menos 3 vocales")
        datos_usuario.clear()
           
    else:
        validar_nombres=True
        
            

while validar_año == False:
    datos_usuario.insert(2,input("\nIngrese el año de su nacimiento: \n"))
    if not datos_usuario[2].isdigit():
        print("El año ingresado debe tener solo numeros\n")
        datos_usuario.pop(2)
    elif len(datos_usuario[2]) !=4:
        print("Año no valido, solo puede ingresar hasta 4 digitos\n")
        datos_usuario.pop(2)
    else:
        validar_año=True

while validar_contra ==False:
    contraseña = input("Ingrese una contraseña: \n")
    if len(contraseña) > 16:
        print("La contraseña es demaciado larga")
    elif len(contraseña) < 8:
        print("La contraseña es demaciado corta")
    elif not any(caracter in caracteres_esp for caracter in contraseña): 
        print("La contrasela deve incluir alguno de estos caracteres: !, @, #, $, %, &") 
    else:
        validar_contra=True

print("Bienvenido", end=" ")
print(datos_usuario[1],end=" ")
print(datos_usuario[0])

    
 
        
    
