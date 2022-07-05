import tkinter

ventana = tkinter.Tk()
ventana.geometry("400x600")
ventana.title("Ejemplo Ventana")
#ventana.iconbitmap('zelda.ico')

#etiqueta = tkinter.Label(ventana, text= "Hola mundo")
#etiqueta.pack()
boton = tkinter.Button(ventana, text="confirmar")
boton.pack()



ventana.mainloop()