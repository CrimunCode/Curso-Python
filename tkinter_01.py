# Imporación de módulos

import tkinter as tk # Tkinter: Módulo para crear a una interfaz gráfica
import os # os: Módulo para acceder a rutas del Sisteme Operativo
from PIL import ImageTk, ImageColor, Image # Pillow: Módulo para procesar imágenes
'''
Descargar e instalar Pillow en la consola
pip install Pillow

Installing collected packages: pillow
Successfully installed pillow-11.0.0

[notice] A new release of pip is available: 24.2 -> 24.3.1 
[notice] To update, run: python.exe -m pip install --upgrade pip
pip install --upgrade pip
'''

# ---Carga de directorios---
# Directorio principal
# carpeta_principal = os.path.dirname("E:/Escritorio/Curso Python/Contenidos") # ruta local del equipo
carpeta_principal = os.path.dirname(__file__) # ruta dinámica en python variable __file__
# print(carpeta_principal)

# Directorio imágenes
carpeta_imagenes = os.path.join(carpeta_principal, "imagenes")
# print(carpeta_imagenes)
carpeta_paisajes = os.path.join(carpeta_imagenes, "paisajes")
# print(carpeta_paisajes)

# Creación de la ventana principal
root = tk.Tk() 

# Tamaño de la ventana principal y ubicación
root.geometry("480x320+1920+320")

# Título de la ventana
root.title("Modulos Tkinker y os")

# Icono de la ventana
root.iconbitmap(os.path.join(carpeta_imagenes, "favicon.ico"))

# Carga de imagen con cambio de resolución
paisaje_01 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_paisajes, "paisaje-01.webp")).resize((480,320)))
etiqueta = tk.Label(image=paisaje_01)
etiqueta.pack()

# Bucle de ejecución
root.mainloop()