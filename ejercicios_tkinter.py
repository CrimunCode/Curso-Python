# Importacion módulo Tkinter
import tkinter as tk

# Creación ventana principal
root = tk.Tk()

# Titulo de la ventana principal
root.title("Ejercicios con Tkinter")

# Tamaño y pocición inicial ventana principal
root.geometry("640x480+1920+320")

# Etiquetas y/o botones
# boton_1 = tk.Button(root, text="Botón 1", command=lambda:crear_etiqueta(1)).pack()
# boton_2 = tk.Button(root, text="Botón 2", command=lambda:crear_etiqueta(2)).pack()
# boton_3 = tk.Button(root, text="Botón 3", command=lambda:crear_etiqueta(3)).pack()
# boton_4 = tk.Button(root, text="Botón 4", command=lambda:crear_etiqueta(4)).pack()

# Etiquetas y botones en Grid Entrada de datos
# Nombre
tk.Label(root, text="Nombre:").grid(row=0, column=0)
entrada_nombre = tk.Entry(root)
entrada_nombre.insert(0, "Escriba su nombre")
entrada_nombre.bind("<Button-1>", lambda e: entrada_nombre.delete(0, tk.END))
entrada_nombre.grid(row=0, column=1)

# Edad
tk.Label(root, text="Edad:").grid(row=1, column=0)
entrada_edad = tk.Entry(root)
entrada_edad.insert(0, "Escriba su edad")
entrada_edad.bind("<Button-1>", lambda e: entrada_edad.delete(0, tk.END))
entrada_edad.grid(row=1, column=1)

# Eventos para los botones

# def crear_etiqueta(numero_boton):
#     etiqueta = tk.Label(root, text=f"Botón {numero_boton} pulsado.")
#     etiqueta.pack()

def saludar():
    # Se obtienen los valores de los Entry
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()
    # se muestra en una etiqueta el valor del Entry
    tk.Label(root, text=f"Mi nombre es: {nombre}. Tengo {edad} años.").grid(row=3, column=1)

tk.Button(root, text="Enviar",command=saludar).grid(row=2, column=1)

# Bucle de ejecución
root.mainloop()