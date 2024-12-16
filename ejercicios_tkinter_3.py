# Importaciones
import random
import tkinter as tk
from tkinter import END, messagebox as mb

# Variables
numero_aleatorio = random.randint(0, 100)
intentos = 1

# Mensaje de inicio del juego
mb.showinfo("Adivina el número", "Ingrese un número de 0 al 100.\n\n¿Cuántos intentos necesitará para conseguir acertar el numero secreto?")

# Ventana, Titulo, Geometria Dimenciones
root = tk.Tk()
root.title("Juego adivinar el número")
root.resizable(False, False)
root.attributes("-topmost", True) # Para que no se vaya hacia a tras la ventana principal
ancho_ventana = 400
alto_ventana = 100

# Pantalla
ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight()

coordenadas_x = int((ancho_pantalla/2) - (ancho_ventana/2))
coordenadas_y = int((alto_pantalla/2) - (alto_ventana/2)) - 37

root.geometry("{}x{}+{}+{}".format(ancho_ventana, alto_ventana, coordenadas_x, coordenadas_y))

# Entrada de Datos (Cuedro de Texto, Etiquetas, Botones)
# Text Box
numero_ingresado = tk.Entry(root)
numero_ingresado.insert(0, "Escriba un número...")
numero_ingresado.bind("<Button-1>", lambda e: numero_ingresado.delete(0, END))
numero_ingresado.pack()
print(numero_aleatorio)

# Evento para el botón
def adivinar_numero():
    global intentos
    try:
        numero = int(numero_ingresado.get())

        if numero < numero_aleatorio:
            mb.showinfo("Fallaste","El número es mayor.")
            intentos+=1
        elif numero > numero_aleatorio:
            mb.showinfo("Fallaste","El número es menor.")
            intentos+=1
        else:
            mb.showinfo("Excelente","Lo has adivinado.")
    except:
        mb.showerror("Error","Valor no válido.")
        intentos+=1

# Botón
tk.Button(root, text="Adivinar", command=adivinar_numero).pack()

# Bucle de ejecuciópn
root.mainloop()