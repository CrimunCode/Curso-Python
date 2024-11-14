#  Calcular el área de un circulo (Pi * radio * radio)

# variables
# radio = float(input("\nIngrese el radio del circulo: "))

# Constantes
PI = 3.14159265359

# Función Lambda
calcular_area = lambda radio : PI * radio * radio

# Llamada a la función
# area = round(calcular_area(radio), 2)

# Mostrar resultado
# print(area)

# Utilizar la sintaxis de declaración y llamada en una linea para mostrar un saludo en la consola con el nombre en un print()

(lambda nombre: print(f"\nQue tal {nombre}!")) ("CrimunCode")

# Mostra esta frase en la consola: El color se encuentra en la posición 1 de la lista con una funcion lambda
colores = ["Rojo","Azul","Amarillo","Verde"]

(lambda color: print(f"\nEl color {color} se encuentra en la posición {colores.index(color)} de la lista."))(color = input("Ingrese un color para buscar su indice: "))