# Importaciones
import tkinter.messagebox as mb

# Capturmos en una variable el valor devuelto por el messagebox
valor = mb.askquestion("Pregunta","¿Que valor entrega cuando seleccionamos si o no?")
# yes, no
# Se muestra el valor por consola
print("\n",valor,"\n") 

# Capturmos en una variable el valor devuelto por el messagebox
valor2 = mb.askyesno("Pregunta","¿Que valor entrega cuando seleccionamos si o no?")
# True, False
# Se muestra el valor por consola
print("\n",valor2,"\n") 

# Capturmos en una variable el valor devuelto por el messagebox
valor3 = mb.askokcancel("Pregunta","¿Que valor entrega cuando seleccionamos Ok o Cancelar?")
# True, False
# Se muestra el valor por consola
print("\n",valor3,"\n")

# Capturmos en una variable el valor devuelto por el messagebox
valor4 = mb.askyesnocancel("Pregunta","¿Que valor entrega cuando seleccionamos Yes, No o Cancelar?") 
# True, False, None
# Se muestra el valor por consola
print("\n",valor4,"\n")

# Capturmos en una variable el valor devuelto por el messagebox
valor5 = mb.askretrycancel("Pregunta","¿Desea Reintentar o Cancelar?") 
# True, False
# Se muestra el valor por consola
print("\n",valor5,"\n")