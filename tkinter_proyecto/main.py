# Impportaciones
import os
import tkinter as tk
from PIL import ImageTk, Image

# Rutas
# Ruta del directorio principal (de este archivo)
carpeta_proyecto = os.path.dirname(__file__)
# print(carpeta_proyecto)

# Rutas imagenes
carpeta_imagenes = os.path.join(carpeta_proyecto, "imagenes")
carpeta_logos = os.path.join(carpeta_imagenes, "logos")
carpeta_iconos = os.path.join(carpeta_imagenes, "iconos")
carpeta_ciudades = os.path.join(carpeta_imagenes, "ciudades")

# Listado imagenes
lista_ciudades = ["ciudad-01.jpg", "ciudad-02.jpg", "ciudad-03.jpg", "ciudad-04.jpg"]

# Tupla vacia para almacenar usuarios nuevos y su contraseña 
usuario_creado = ()

# Ciclo para crear un nombre de usuario
while True:
    nuevo_usuario_1 = input("\nIngrese un nombre para el nuevo usuario. : ")
    nuevo_usuario_2 = input("\nRepita nuevamente el nombre de usuario. : ")
    nueva_contrasena_1 = input("\nIngrese una contraseña. : ")
    nueva_contrasena_2 = input("\nRepita nuevamente la contraseña. : ")
    
    if nuevo_usuario_1 != nuevo_usuario_2 or nueva_contrasena_1 != nueva_contrasena_2:
        print("Los valores no coinciden, vuelva a intentarlo.")
    else:
        usuario_creado = (nuevo_usuario_1,nueva_contrasena_1)
        break

# Ventana principal
v1 = tk.Tk()

# Titulo ventana principal
v1.title("Agencia de Viajes Tkinter")

# Tamaño y Pocición de la ventana principal (opcional)

# Icono en ventana principal
v1.iconbitmap(os.path.join(carpeta_iconos, "favicon.ico"))

# Contenido ventana principal
# Logo
logo = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_logos, "logo_agencia_2.png")).resize((300,400)))
etiqueta_logo = tk.Label(image=logo)
etiqueta_logo.grid(row=0, column=0)

# Campos de texto
# Usuario
tk.Label(text="Usuario").grid(row=1, column=0)
usuario = tk.Entry()
usuario.grid(row=2, column=0)
usuario.insert(0, "Ej:Cristian")
usuario.bind("<Button-1>", lambda e: usuario.delete(0, tk.END))

# Contraseña
tk.Label(text="Contraseña").grid(row=3, column=0)
contrasena = tk.Entry()
contrasena.insert(0, "*"*7)
contrasena.bind("<Button-1>", lambda e: contrasena.delete(0, tk.END))
contrasena.grid(row=4, column=0)

# Validación Login
def validar_login():
    obtener_usuario = usuario.get()
    obtener_contrasena = contrasena.get()
    
    if obtener_usuario != usuario_creado[0] or obtener_contrasena != usuario_creado[1]:
        tk.Label(text="ERROR: Usuario o Contraseña incorrectos.").grid(row=6, column=0)
    else:
        tk.Label(text=f"Hola, {usuario_creado[0]}. Espera unos instantes...   ").grid(row=6, column=0)

# Botón Enviar
tk.Button(v1, text="Enviar", command=validar_login).grid(row=5, column=0)

# Bucle de ejecución
v1.mainloop()