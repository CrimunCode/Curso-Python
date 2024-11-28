# Ejercicios 2 con Tkinter

# Importaciones
import tkinter as tk

# Ventana principal
root = tk.Tk()
# Titulo ventana principal
root.title("Ejercicios 2 con Tkinter")
# Tamaño y ubicación de la ventana principal

# Etiquetas de Marcos

# Ejercicio 1
'''
marco_1 = tk.LabelFrame(root,
                        text = "Ejercicios 2 con Tkinter",
                        width = 300,
                        height = 300,
                        )
marco_1.pack(padx=25, pady=10)
'''

# Ejercicio 2
'''
marco_1 = tk.LabelFrame(root,
                        background="orange red",
                        width=200,
                        height=400,
                        border=0,
                        )
marco_1.grid(row=0, column=0)

marco_2 = tk.LabelFrame(root,
                        background="RoyalBlue1",
                        width=200,
                        height=400,
                        border=0,
                        )
marco_2.grid(row=0, column=1)
'''

# Ejercico 3
marco_blanco = tk.LabelFrame(root, background="khaki", width=50, height=50, border=0)
marco_blanco.grid(row=0, column=0)

marco_gris = tk.LabelFrame(root, background="gray", width=50, height=50, border=0)
marco_gris.grid(row=0, column=1)

marco_blanco = tk.LabelFrame(root, background="khaki", width=50, height=50, border=0)
marco_blanco.grid(row=0, column=2)

marco_gris = tk.LabelFrame(root, background="gray", width=50, height=50, border=0)
marco_gris.grid(row=1, column=0)

marco_blanco = tk.LabelFrame(root, background="khaki", width=50, height=50, border=0)
marco_blanco.grid(row=1, column=1)

marco_gris = tk.LabelFrame(root, background="gray", width=50, height=50, border=0)
marco_gris.grid(row=1, column=2)

marco_blanco = tk.LabelFrame(root, background="khaki", width=50, height=50, border=0)
marco_blanco.grid(row=2, column=0)

marco_gris = tk.LabelFrame(root, background="gray", width=50, height=50, border=0)
marco_gris.grid(row=2, column=1)

marco_blanco = tk.LabelFrame(root, background="khaki", width=50, height=50, border=0)
marco_blanco.grid(row=2, column=2)

# Bucle de ejecución
root.mainloop()