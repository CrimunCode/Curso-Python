# Ejercicios con Radiobuttons en Tkinter 

# Importaciones
import tkinter as tk
import os
from PIL import ImageTk, Image

# Ventana
root = tk.Tk()
# Titulo ventana
root.title("Ejercicios con Radiobuttons en Tkinter")
# Tamaño de la ventana
# root.geometry("420x480")
# Color de fondo de la ventana
root.configure(background="AntiqueWhite3")

# Rutas
# Ruta del proyecto
ruta_proyecto = os.path.dirname(__file__)
# Ruta de las imagenes
ruta_imagenes = os.path.join(ruta_proyecto, "imagenes")
ruta_usuarios = os.path.join(ruta_imagenes, "usuarios")
ruta_iconos = os.path.join(ruta_imagenes, "iconos")

# Icono de la Ventana principal
root.iconbitmap(os.path.join(ruta_iconos, "login.ico"))

# Marcos o Frames

marco_1 = tk.LabelFrame(root,
                        text="Selecciones un usuario :",
                        # padx=5,
                        # pady=5,
                        # width=300,
                        # height=300,
                        background="gray98",
                        border=0,
                        ).grid(row=0, column=0, padx=5, pady=5)


# Variables
# Variable de control para los Radiobutton
# usuario = tk.IntVar() # Se camvio pos StringVar, por que ahora se necesita obtener, el nombre del usuario (de la variable value de los Radiobutton), en vez del numero que antes tenía
usuario = tk.StringVar()
usuario.set("Error")

# Cargar imagenes en pantalla
emma = ImageTk.PhotoImage(Image.open(os.path.join(ruta_usuarios, "emma.jpg")).resize((200,200)))
label = tk.Label(root, image=emma, background="gray98")
label.grid(row=0, column=0, padx=30, pady=5)

tk.Radiobutton(root,
               text="Emma",
               variable=usuario,
               value="Emma",
               background="plum1",
               ).grid(row=1, column=0)

jacob = ImageTk.PhotoImage(Image.open(os.path.join(ruta_usuarios, "jacob.jpg")).resize((200,200)))
label = tk.Label(root, image=jacob, background="gray98")
label.grid(row=0, column=1, padx=30, pady=5)

tk.Radiobutton(root,
               text="Jacob",
               variable=usuario,
               value="Jacob",
                background="light blue",
               ).grid(row=1, column=1)

noah = ImageTk.PhotoImage(Image.open(os.path.join(ruta_usuarios, "noah.jpg")).resize((200,200)))
label = tk.Label(root, image=noah, background="gray98")
label.grid(row=2, column=0, padx=30, pady=5)

tk.Radiobutton(root,
               text="Noah",
               variable=usuario,
               value="Noah",
               background="khaki1",
               ).grid(row=3, column=0)

sophia = ImageTk.PhotoImage(Image.open(os.path.join(ruta_usuarios, "sophia.jpg")).resize((200,200)))
label = tk.Label(root, image=sophia, background="gray98")
label.grid(row=2, column=1, padx=30, pady=5)

tk.Radiobutton(root,
               text="Sophia",
               variable=usuario,
               value="Sophia",
               background="HotPink1",
               ).grid(row=3, column=1)

# Funciones
def actualizar_radiobutton():
    if usuario.get() == "Error":
        tk.Label(root, text="¡No has seleccionado ninguna cuenta!\nInténtalo de nuevo.", foreground="red2").grid(row=4 , column=1)
    else:
        tk.Label(root, text="¡No has seleccionado ninguna cuenta!\nInténtalo de nuevo.", foreground="AntiqueWhite3", background="AntiqueWhite3").grid(row=4 , column=1)
        tk.Label(root, text=f"Hola {usuario.get()}. Accediendo a tu cuenta personal...", background="gray98").grid(row=4, column=1)

# Boton Entrar
boton_entrar = tk.Button(root, text="Entrar", command=actualizar_radiobutton).grid(row=4, column=0, padx=5, pady=15)

# Bucle de ejecución
root.mainloop()