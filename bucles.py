# Bucle for con rango de término (del 0 a "x", donde la posición 0 se incluye y 'x' es la última picición y no se incluye )
for i in range(5):
    print(f"El valor del bucle es: {i}.")
print("\n")

# Bucle for con rango de inicio y término (de "x" a "y", donde "x" se incluye pero "y" no se incluye)
for i in range(3,7):
    print(f"El valor del bucle es: {i}.")
print("\n")

# Bucle for con rango de inicio y término con cambio de incremento (de "x" a "y", donde "x" se incluye pero "y" no se incluye)
for i in range(0,11,2):
    print(f"El valor del bucle es: {i}.")
print("\n")

# Bucle for con rango de inicio y término con cambio de decremento (de "x" a "y", donde "x" se incluye pero "y" no se incluye)
for i in range(10,-2,-2):
    print(f"El valor del bucle es: {i}.")
print("\n")

# Iterar Listas o tuplas con bucles
colores = ['Rojo', 'Azul', 'Verde', 'Amarillo']
print("---LISTADO DE COLORES---")

for color in colores:
    print(f"-{color}")
print("\n")

# Omitir ciertas ejecuciones en el bucle (uso de condicionales y del continue, para omitir lo que cumple la condición y pasar a la siguiente linea de código)
colores = ['Rojo', 'Azul', 'Verde', 'Amarillo']
print("---LISTADO DE COLORES---")

for color in colores:
    if color == "Azul" or color == "Verde":
        print("Se ha saltado este valor")
        continue
    print(f"-Color {color}.")
print("\n")

# Terminar el bucle antes de tiempo break
colores = ['Rojo', 'Azul', 'Verde', 'Amarillo']
print("---LISTADO DE COLORES---")

for color in colores:
    if color == "Azul":
        print("Se ha roto la ejecución del bucle")
        break
    print(f"-Color {color}.")
print("\n")

# Bucle while
i = 1

while i <= 5:
    print(f"El valor del bulce es: {i}.")
    i += 1
print("\n")

# Bucle do while, no existe en Python, pero se puede simular
while True:
    salida = input("Indrese 'salir' para finalizar. \n").lower()
    if salida == 'salir':
        break
