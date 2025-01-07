# Método __init__ (Atributos de instancia) con valores instanciados

class Usuario:
    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def describe(self):
        print(f"\nNombre   : {self.nombre}.")
        print(f"Apellidos: {self.apellidos}.")
        print(f"Edad     : {self.edad}.")

usuario1 = Usuario("Cristian", "Muñoz Neira", "40") # Instancia del objeto

usuario1.describe()

# Método __init__ (Atributos de instancia) con valores por defecto
class Usuario:
    def __init__(self, nombre="Usuario por Defecto", apellidos="Apellidos por Defecto", edad="Sin datos"):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def describe(self):
        print(f"\nNombre   : {self.nombre}.")
        print(f"Apellidos: {self.apellidos}.")
        print(f"Edad     : {self.edad}.")

usuario1 = Usuario() # Instancia del objeto

usuario1.describe()

# Método __init__ (Atributos de instancia) con valores instanciados y por defecto
class Usuario:
    def __init__(self, nombre="Usuario por Defecto", apellidos="apellidos por defecto", edad="Sin datos"):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def describe(self):
        print(f"\nNombre   : {self.nombre}.")
        print(f"Apellidos: {self.apellidos}.")
        print(f"Edad     : {self.edad}.")

usuario1 = Usuario("Pedro", "Perez") # Instancia del objeto

usuario1.describe()

# Método __init__ (Atributos de instancia) con valores instanciados con un diccionario
class Usuario:
    def __init__(self, nombre="Usuario por Defecto", apellidos="apellidos por defecto", edad="Sin datos"):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def describe(self):
        print(f"\nNombre   : {self.nombre}.")
        print(f"Apellidos: {self.apellidos}.")
        print(f"Edad     : {self.edad}.")

usuario1 = Usuario(edad="27", apellidos="Perez") # Instancia del objeto con un diccionario

usuario1.describe()

# Método __init__ (Atributos de instancia) con valores nuevos instanciados
class Usuario:
    def __init__(self, telefono, nombre="Usuario por Defecto", apellidos="apellidos por defecto", edad="Sin datos"):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.telefono = telefono

    def describe(self):
        print(f"\nNombre   : {self.nombre}.")
        print(f"Apellidos: {self.apellidos}.")
        print(f"Edad     : {self.edad}.")
        print(f"Teléfono :{self.telefono}")

usuario1 = Usuario("5554443", edad="27", apellidos="Perez") # Instancia del objeto con un diccionario

usuario1.describe()