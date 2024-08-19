# Bucle While : estructura que se repite mientras la condición sea verdadera.

"""
x = 1
while x <= 10:
    print(f"Hola a todos, estoy dentro de un buble y x vale {x}")
    x += 1

# BREAK : se sale del bucle
x = 1
while x <= 10:
    print(f"Hola a todos, estoy dentro de un buble y x vale {x}")
    if x == 5:
        break
    x += 1
print(f"Fuera del bucle x vale: {x}")

# CONTINUE : se salta la linea siguiente cuando se cumple la condición
x = 0
while x < 10:
    x += 1
    if x == 5:
        continue
    print(f"Hola a todos, estoy dentro de un bucle y x vale {x}")
print(x)
"""
# Ejemplo Práctico

while True:
    print("Desea salir de este menú")
    respuesta = input("Para confirmar presione (s/n)").strip().lower()
    if respuesta == "s":
        break