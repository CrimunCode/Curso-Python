# Modulos: librerías con código que ayudan a facilitar la programación.
# Modulo para trabajar con interfaces gráficas Tkinter
# Widget: componentes para ir agregando al programa
# Alias, para no tener que escribir siempre Tkinter
# Tambien se puede trabajar importando todo, para no tener que escribir el alias del módulo

# Importaciones sin alias
# import tkinter

# Importaciones con alias
import tkinter as tk

# importar todo para no tener que escribir el alias del módulo
# from tkinter import *

# Creación de la ventana principal
root = tk.Tk()

# Cambiar el título de la ventana
root.title("Curso de Tkinter en Programación con Python")

# Tamaño y pocición inicial de la ventana de Tkinter
# root.geometry("800x600")

# Cambiar las coordenadas de aparición en la pantalla de la ventana de Tkinter
root.geometry("800x600+560+240")

# Creación de las etiquetas
mensaje = tk.Label(root, text="Mi 1º etiqueta con Tkinter.")
mensaje_2 = tk.Label(root, text="Mi 2º etiqueta con Tkinter.")

# no se pueden utilizar un mismo mensaje con ambos métodos pack() y grid()
# Metodo pack() de Tkniter
# mensaje.pack() 
# mensaje_2.pack()

# Método grid() de Tkinter (solo surgen columnas si hay elementos)
# title 0 titulo
# label = etiqueta
# root = raiz
# text = texto
# pack = empaquetar
# grid = cuadrícula
# mainloop = bucle principal
# row = fila
# column = columna

# Muestrar las eqiquetas
mensaje.grid(row=0, column=0)
mensaje_2.grid(row=0, column=1)

# Aplicar el método grid() en la misma línea de la declaración del widget
mensaje = tk.Label(root, text="Mi 1º etiqueta con Tkinter.").grid(row=1, column=0)
mensaje_2 = tk.Label(root, text="Mi 2º etiqueta con Tkinter.").grid(row=1, column=1)

# Bucle de ejecución: hay que hacer un bucke, para que se aprecie la ventana
root.mainloop()
