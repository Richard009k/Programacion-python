from tkinter import *
from math import *
 
#ver operacion en pantalla
def btnClik(num):
    global operador
    operador=operador+str(num)
    input_text.set(operador)
 
#calcular y mostrar resultado
def resultado():
    global operador
    try:
        opera=str(eval(operador))
        input_text.set(opera)
    except:
        input_text.set("ERROR")
    operador = ""
 
#limpiar pantalla
def clear():
    global operador
    operador=("")
    input_text.set("0")
 
 
ventana=Tk()
ventana.title("CALCULADORA")
ventana.iconbitmap("calcu.ico")
ventana.geometry("390x500")
ventana.configure(background="gray40")
color_boton=("gray90")
 
ancho_boton=11
alto_boton=3
input_text=StringVar()
operador=""
 
Salida=Entry(ventana,font=("Helvetica",15,'bold'),width=33,
textvariable=input_text,insertwidth=10,bg="gray100",justify="right")
Salida.place(x=10,y=60)
 
#BOTONES
Button(ventana,text="0",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=107,y=420)
Button(ventana,text="1",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(1)).place(x=17,y=360)
Button(ventana,text="2",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(2)).place(x=107,y=360)
Button(ventana,text="3",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(3)).place(x=197,y=360)
Button(ventana,text="4",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(4)).place(x=17,y=300)
Button(ventana,text="5",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(5)).place(x=107,y=300)
Button(ventana,text="6",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(6)).place(x=197,y=300)
Button(ventana,text="7",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(7)).place(x=17,y=240)
Button(ventana,text="8",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(8)).place(x=107,y=240)
Button(ventana,text="9",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(9)).place(x=197,y=240)
Button(ventana,text="π",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("pi")).place(x=107,y=120)
Button(ventana,text=".",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(".")).place(x=17,y=420)
Button(ventana,text="+",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("+")).place(x=287,y=360)
Button(ventana,text="-",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("-")).place(x=287,y=300)
Button(ventana,text="*",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("*")).place(x=287,y=240)
Button(ventana,text="/",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("/")).place(x=287,y=180)
Button(ventana,text="√",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("sqrt(")).place(x=17,y=120)
Button(ventana,text="(",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("(")).place(x=17,y=180)
Button(ventana,text=")",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(")")).place(x=107,y=180)
Button(ventana,text="%",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("%")).place(x=197,y=120)
Button(ventana,text="ln",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("log(")).place(x=197,y=180)
Button(ventana,text="C",bg=color_boton,width=ancho_boton,height=alto_boton,command=clear).place(x=287,y=120)
Button(ventana,text="EXP",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("**")).place(x=197,y=420)
Button(ventana,text="=",bg=color_boton,width=ancho_boton,height=alto_boton,command=resultado).place(x=287,y=420)
 
clear()
 
ventana.mainloop()