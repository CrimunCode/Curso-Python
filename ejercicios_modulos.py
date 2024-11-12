# Importaciones:

# import tkinter # Forma 1
import tkinter as tk # Forma 2
# from tkinter import * # Forma 3

# Creación de la ventana principal
# root = tkinter.Tk()
# root = tk.Tk()
root = tk.Tk()

# Título de la ventana
root.title("Ejercicios en Tkinter")

# Tamaño de la ventana
root.geometry("600x450+50+75")

# Creación de las etiquetas
msj1 = tk.Label(root, text="Mensaje 1")
msj2 = tk.Label(root, text="Mensaje 2")

# Mostrar etiquetas
msj1.grid(row=0, column=0)
msj2.grid(row=0, column=1)

# Bucle de ejecución
root.mainloop()