# Importaciones
import random
import tkinter as tk

numero_aleatorio = random.randint(0, 100)
print("\n", numero_aleatorio, "\n")
print("Se ha generado un número aleatorio entre e 0 y el 100")
intentos = 0

while True:
    numero_ingresado = input("Ingresa un número para tratar de adivinarlo: ")
    if numero_ingresado.isdigit():
        numero_ingresado = int(numero_ingresado)
        if numero_ingresado == numero_aleatorio:
            intentos += 1
            print(f"\nFelicidades ¡has adivinado! en {intentos} intentos.\nEl número aleatorio era el: '{numero_aleatorio}'.")
            break
        elif numero_aleatorio < numero_ingresado:
            intentos += 1
            print(f"\nEl numero aleatorio es MENOR al numero '{numero_ingresado}'")
        elif numero_aleatorio > numero_ingresado:
            intentos += 1
            print(f"\nEl numero aleatorio es MAYOR al numero '{numero_ingresado}'")
    else:
        error = str(numero_ingresado)
        print(f"\nError: lo ingresado ({numero_ingresado}) no es un número válido.\nNúmeros válidos entre el 0 y el 100")