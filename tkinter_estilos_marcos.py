# Iniciación a los estilos y marcos de Tkinter

# Imortaciones
import tkinter as tk

# Ventana principal
root = tk.Tk()
# Titulo de la ventana
root.title("Estilos y marcos de Tkinter")
# Tamaño y ubicación ventana
# root.geometry("320x240+2200+400")

# Marco o frame
marco1 = tk.LabelFrame(root, 
                      text="Entrada de datos",
                      padx=20,
                      pady=20,
                      )
marco1.grid(row=0, column=0, padx=15, pady=15)

marco2 = tk.LabelFrame(root,
                      text="Enviar",
                      padx=20,
                      pady=20,
                      )
marco2.grid(row=1, column=0, padx=5, pady=15) # Padding para el marco con respecto a la ventana

marco3 = tk.LabelFrame(root,
                      text="Resultado",
                      padx=20,
                      pady=20,
                      )
marco3.grid(row=2, column=0, padx=5, pady=15) # Padding para el marco con respecto a la ventana

# Entrada de datos
entrada = tk.Entry(marco1, 
                   background="chocolate1", # Color de fondo
                   border=5, # Borde
                   foreground="Blue3", # color de la fuente
                   width=30, # Ancho en tamaño de carácteres
                   )
entrada.pack()
entrada.insert(0, "Ecriba su nombre...")
entrada.bind("<Button-1>", lambda e: entrada.delete(0, tk.END))

# Funciones
def f_enviar():
    nombre = entrada.get()
    tk.Label(marco3, 
             text=f"Hola {nombre}",
             background="skyblue",
             width=27, # Ancho en pixeles
             ).pack()
    entrada.delete(0, tk.END)
    entrada.insert(0, "Escriba su nombre...")

# Boton enviar
btn = tk.Button(marco2, 
                text="Enviar", 
                command=f_enviar,
                background="deepskyblue",
                foreground="gray98",
                border=3,
                width=26, # Ancho en pixeles
                ).pack()

# Bucle de ejecución
root.mainloop()