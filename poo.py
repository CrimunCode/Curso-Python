# Programación orientada a Objetos: un paradigma de programación, en la que todo lo que se quiere representar en un sistema, se puede parametrizar con las clases, esto permite reutilizar el código.
#  Las clases: un sistema que genera objetos, parecidos pero que cada uno tiene sus propias características que los hacen únicos. La clases están compuestas por un nombre, atributos con sus valores y los métodos.

# Declarar clases en Python (Pascal Case)
# Atributos: son variables que están dentro de una clase
# Atributos = Valores (valores de clase o valores por defecto se heredan a tosdos los objetos creados)

class Taza():
    color = "Blanco"
    mensaje = None
    material = "Porcelana"
    limpia = True

# Instanciar un objeto: cuando se crea un objeto a partir de una clase (solo se crean en tiempo de ejecución del programa se crean en la memoria RAM y si el programa se cierra se borran los objetos)
taza_1 = Taza()
taza_2 = Taza()

# Ver direcciones de memoria donde estan almacenados los objetos
print(f"\n{taza_1}")
print(f"\n{taza_2}")

# Acceder a los atributos de los objetos
print(f"\n{taza_1.color}")
print(f"\n{taza_2.color}")

# Valores por defecto en las clases (herencia)
# Reasignar valores a atributos de objetos
taza_2.color = "Negro"
print(f"\n{taza_2.color}")

# Métodos de las clases: son funciones que pertenecen a un clases, son las acciones de la clase
# Revisar el tipo de una clase
numeros = [1,3,5,7]

print(f"\n{type(numeros)}")

# Como se declara un método de una clase
# Se declara la clase vehiculo
class Vehiculo():
    # Atributos = Valores (valores de clase o valores por defecto se heredan a tosdos los objetos creados)    color = None
    longitud_metros = None
    ruedas = 4

    # Métodos
    def arrancar(self):
        print("\nEl vehículo ha arrancado.")
    
    def detener(self):
        print("\nEl vehículo está detenido.")

# Instanciar los objetos
vehiculo_1 = Vehiculo()
vehiculo_2 = Vehiculo()

# Crear atributos de un objeto en concreto (atributos que no están definidos en la clase)
vehiculo_2.material_aleron = "Fibra de carbono"

# Llamadas a los métodos
vehiculo_1.arrancar()
vehiculo_1.detener()

print(f"\n{vehiculo_2.material_aleron}")

# Atributos de instancia (Método __init__ de python)
class Vehiculo2():
    # Atributos = Valores (valores de clase o valores por defecto se heredan a tosdos los objetos creados)
    procedencia = "Alemania"

    # Metodo __init__ (atributos de instancia)
    def __init__(self, color, longitud_metros, ruedas):
        self.color = color
        self.longitud_metros = longitud_metros
        self.ruedas = ruedas

    # Métodos
    def arrancar(self):
        print("\nEl vehículo ha arrancado.")
    
    def detener(self):
        print("\nEl vehículo está detenido.")

    def mostrar_info(self):
        print(f"\nVehículo de color {self.color}. Con una longitud de {self.longitud_metros} metros y {self.ruedas} ruedas y su pais de origen es: {self.procedencia}.")

# Instanciar los objetos
vehiculo_3 = Vehiculo2("Rojo", 4, 4)
vehiculo_4 = Vehiculo2("Negro", 8.25 ,8)

# Mostar los objetos creados de la clase Vehiculo2 (este nombre se puso solo para no tener que borrar la clase Vehiculo de los ejemplos anteriores)
print(f"\nColor Vehiculo 3: {vehiculo_3.color}\nLongitud Vehiculo 3: {vehiculo_3.longitud_metros}\nNº de ruedas Vehiculo 3: {vehiculo_3.ruedas}\nPais de origen: {vehiculo_3.procedencia}.")
print(f"\nColor Vehiculo 4: {vehiculo_4.color}\nLongitud Vehiculo 4: {vehiculo_4.longitud_metros}\nNº de ruedas Vehiculo 4: {vehiculo_4.ruedas}\nPaís de origen: {vehiculo_4.procedencia}.")

# Self: Se refiere al objeto que será instanciado de la clase
vehiculo_3.mostrar_info()
vehiculo_4.mostrar_info()

# Estructucas vacías (clase vacía)
class Vehiculo():
    pass 