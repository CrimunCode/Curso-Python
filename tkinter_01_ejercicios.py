# Impportaciones
import os
import tkinter as tk
from PIL import ImageTk, Image

# Ruta del directorio principal (de este archivo)
carpeta_principal = os.path.dirname(__file__) # print(ruta)

# Crear ventana principal
root = tk.Tk()

# Titulo de la ventana principal
root.title("Ejercicios Tkinter - 01")

# Fijar resolución y ubicación de la ventana principal
# root.geometry("480x320+3210+320")

# Directorio imágenes 
lista_imagenes = ["paisaje-01.jpg", "paisaje-02.jpg", "paisaje-03.jpg", "paisaje-04.jpg"]   # Esta lista se creo para referenciar (más abajo) los nombres de las imagánes con el índice de la lista
carpeta_imagenes = os.path.join(carpeta_principal, "imagenes")
carpeta_paisajes = os.path.join(carpeta_imagenes, "paisajes")

# Icono de la Ventana principal
root.iconbitmap(os.path.join(carpeta_imagenes, "imagenes.ico"))

# Cargar imagenes en pantalla con cambio de resolución
paisaje_01 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_paisajes, f"{lista_imagenes[0]}")).resize((400,250)))
etiqueta_01 = tk.Label(image=paisaje_01)
etiqueta_01.grid(row=0, column=0)

paisaje_02 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_paisajes, f"{lista_imagenes[1]}")).resize((400,250)))
etiqueta_02 = tk.Label(image=paisaje_02)
etiqueta_02.grid(row=0, column=1)

paisaje_03 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_paisajes, f"{lista_imagenes[2]}")).resize((400,250)))
etiqueta_03 = tk.Label(image=paisaje_03)
etiqueta_03.grid(row=1, column=0)

paisaje_04 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_paisajes, f"{lista_imagenes[3]}")).resize((400,250)))
etiqueta_04 = tk.Label(image=paisaje_04)
etiqueta_04.grid(row=1, column=1)

# Bucle de ejecución
root.mainloop()