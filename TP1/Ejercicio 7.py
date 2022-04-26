# Ejercicio 7 - Ricardo Vaja
nombre= input("Ingrese su nombre: ")
apellido= input("ingrese su apellido: ")
edad= int(input("Ingrese su edad: "))
billetera= int(input("ingrese el dinero que tiene en su billetera: "))
hambre= int(input("ingrese del 0 al 10 el hambre que tiene: "))

if edad < 35:
    print(f"Hola {nombre}. Eres una persona joven ya que tu edad es {edad}.")

elif edad >34 and billetera > 500:
    print(f"Hola {nombre} {apellido} ¿Hoy hay asado?")

elif hambre > 7 or billetera < 100 and edad < 18:
    print(f"Hola {nombre} {apellido}- ¿Vas a comer a lo de tus padres?")