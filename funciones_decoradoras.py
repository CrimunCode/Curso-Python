# Funciones decoradoras
# Estructura básica de una función decoradora
'''
def a(b): # Función Decoradora
    def c():
        # código de la función c
        b() # Función externa (llamada a la función parámetro)
        # Función Interna (código después de la llamada)
    return c
'''
    
# Otra forma de representar la función decoroadora
# def a(b) -> c

# Como construir una función decoradora
def funcion_decoradora(b):
    def c():
        print(f"\nEl resultado de la operación {b.__name__} es: ")
        b()
        print("Operación realizada con éxito.")
    return c

# variables gobales
a = 50
b = 10

@funcion_decoradora
def sumar():
    print(a + b)

@funcion_decoradora
def restar():
    print(a  - b)

@funcion_decoradora
def multiplicar():
    print(a * b)

@funcion_decoradora
def dividir():
    print(a / b)

sumar()
restar()
multiplicar()
dividir()