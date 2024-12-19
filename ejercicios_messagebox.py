# Importaciones
import tkinter.messagebox as mb

# Capturar en una variable el valor devuelto por el messagebox
valor = mb.askyesnocancel("Pregunta","¿1 + 1 = 2?")

if valor: # if valor = True
    mb.showinfo("Correcto","1 + 1 = 2 \n\n 👍🏼")
elif valor is False:
    mb.showerror("Incorrecto","¡Lástima, te has equivocado!")
else:
    mb.showwarning("Cancelar","¿Tal ves en otro momento?")