# Radiobuttons en Tkinter

# Importaciopnes
import tkinter as tk

# Ventana Principal
root = tk.Tk()
# Titulo ventana
root.title("Rabiobuttons en Tkinter")

opcion = tk.IntVar() # Variable de control, para relacionar con los Radiobuttons entre si
opcion.set(2) # Para establecer una opcion predeterminada

# Funciones
# Función para el botón de envío
def actualizar_radio(valor):
    tk.Label(root, text=valor).pack()

# Radiobutton
tk.Radiobutton(root,
               text="Rojo",
               variable=opcion,
               value=1,
               ).pack()

tk.Radiobutton(root,
               text="Azul",
               variable=opcion,
               value=2,
               ).pack()

tk.Radiobutton(root,
               text="Verde",
               variable=opcion,
               value=3,
               ).pack()

tk.Radiobutton(root,
               text="Amarillo",
               variable=opcion,
               value=4,
               ).pack()

# tk.Label(root, text=f"{opcion.get()}").pack() # para mostrar el valor de la variable opcion

# Botón de envío
boton_envia = tk.Button(root,
                        text="Enviar",
                        command=lambda:actualizar_radio(opcion.get())).pack()

# Bucle de ejecución
root.mainloop()