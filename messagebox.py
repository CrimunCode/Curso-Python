# Importaciones
import tkinter as tk
from tkinter.messagebox import *

# Ventana principal
root = tk.Tk()
# Titulo ventana
root.title("Messagebox de Tkinter")

# Funcion para mensajes 
def mostrar_informacion():
    showinfo("Mensaje:","Este el el mensaje que se muestra en la ventana.")

# Funcion para mensaje de alerta
def mostrar_advertencia():
    showwarning("Precaución:","La acción que está tratando de realizar, no se puede deshacer.")

# Funcion para mensaje de error
def mostrar_error():
    showerror("Error:","Imposible realizar esta acción. Error 300, cuando el problema está entre el teclado ⌨ y el asiento 💺 (👨‍🦱)...")

# Funcion para mensaje de pregunta
def mostrar_pregunta():
    askquestion("Pregunta:","¿Sabias que? El cielo lo vemos azul debido a la dispersión de la luz solar.")

# Funcion para mensaje de pregunta si o no
def mostrar_preguntasino():
    askyesno("Pregunta si o no:","¿Sabias que? El cielo lo vemos azul debido a la dispersión de la luz solar.")

# Funcion para mensaje de pregunta ok o cancelar
def mostrar_preguntaokcancel():
    askokcancel("Pregunta Ok / Cancelar:","¿Seguro que desea continuar?\n\nLa acción que va a realizar, podría comprometer la integridad de la Base de Datos.")

# Funcion para mensaje de pregunta Si, No o cancelar
def mostrar_preguntayesnocancel():
    askyesnocancel("Pregunta Si , No o Cancelar:","¿Seguro que desea continuar?\n\nLa acción que va a realizar, podría comprometer la integridad de la Base de Datos.")

# Funcion para mensaje de pregunta Si, No o cancelar
def mostrar_preguntareintentarcancelar():
    askretrycancel("Pregunta Reintentar o Cancelar:","¡Algo salió mal!\n\nLa acción no se pudo completar.")

# Botónes para llamar a las funciónes
boton = tk.Button(root, text="Mostrar Mensaje", width=75, command=mostrar_informacion).pack()
boton = tk.Button(root, text="Mostrar Advertencia", width=75, command=mostrar_advertencia).pack()
boton = tk.Button(root, text="Mostrar Error", width=75, command=mostrar_error).pack()
boton = tk.Button(root, text="Mostrar Pregunta", width=75, command=mostrar_pregunta).pack()
boton = tk.Button(root, text="Mostrar Pregunta Si o No", width=75, command=mostrar_preguntasino).pack()
boton = tk.Button(root, text="Mostrar Pregunta Ok o Cancelar", width=75, command=mostrar_preguntaokcancel).pack()
boton = tk.Button(root, text="Mostrar Pregunta Si, No o Cancelar", width=75, command=mostrar_preguntayesnocancel).pack()
boton = tk.Button(root, text="Mostrar reintentar o Cancelar", width=75, command=mostrar_preguntareintentarcancelar).pack()

# Bucle de ejecución
root.mainloop()