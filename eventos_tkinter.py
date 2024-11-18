# Importaciones
import tkinter as tk

# Creaciación de la ventana principal
root = tk.Tk()

# Titulo de la ventana
root.title("Eventos en Tkinter")

# Entrada de datos
entrada = tk.Entry(root)
entrada.insert(0, "Escriba su nombre...")
entrada.bind("<Button-1>", lambda e : entrada.delete(0, tk.END)) #  Se activa la función delete cuando hacemos click con el boton izquierdo del mouse
# entrada.bind("<BackSpace>", lambda e : entrada.delete(0, tk.END)) #  Se activa la función delete cuando hacemos click con el boton borrar del teclado
# entrada.bind("<Key>", lambda e : entrada.delete(0, tk.END)) # Se activa la funcion delete si precionamos cualquier tecla
entrada.pack()

# Evento para el botón
def pulsar_boton():
    # print("Botón pulsado.")
    nombre = entrada.get()
    tk.Label(root,text=f"{nombre}").pack()

# Botón
tk.Button(root, text="Enviar", command=pulsar_boton).pack() # Boton_1 = tk.Button(......) Puede ser guardado en una variable, no es obligatorio

# Bucle de ejecución
root.mainloop()