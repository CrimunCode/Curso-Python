# Centrar Ventanas en Tkinter y Redimensionado

# Importaciones
import tkinter as tk

# --- VENTANA PRINCIPAL ---> root

# Ventana principal
root = tk.Tk()
# Titulo ventana
root.title("Centrar Ventanas y Redimensionado en Tkinter")
# Redimencionado de la ventana
root.resizable(False, False)
ancho_ventana = 500
alto_ventana = 400

# Pantalla
ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight()

tk.Label(text=f"Ancho Pantalla: {ancho_pantalla} píxeles.").pack()
tk.Label(text=f"Alto Pantalla: {alto_pantalla} píxeles.").pack()

coordenadas_x = int((ancho_pantalla/2)-(ancho_ventana/2))
coordenadas_y = int((alto_pantalla/2)-(alto_ventana/2))

# Ubicacion y posición
root.geometry("{}x{}+{}+{}".format(ancho_ventana, alto_ventana, coordenadas_x, coordenadas_y))

# Ajustes
root.eval('tk::PlaceWindow . center')

# Ventana maximizada
# root.state("zoomed")

# --- WIDGETS ---> root

# Entrada de datos
entrada = tk.Entry(root).pack()

# Botón enviar
boton = tk.Button(root, text="Enviar").pack()

# Bucle de ejecución
root.mainloop()