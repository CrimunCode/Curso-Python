colores = ["Rojo", "Verde", "Amarillo"]

def agregar_color(color):
    colores.insert(0, color)

agregar_color(input("Escriba un color para añadirlo a la lista:\n"))

print(colores)

def saludar():
    nombre = input("Introduzca su nombre, por favor\n")
    print(f"¡Muy buenas, {nombre}!")
saludar()

