# Una función normal
def saludar():
    nombre = input("\nIntoduzca su nombre, por favor\n")
    print(f"\n¡Muy buenas, {nombre}!\n")
saludar()

# Función con parámetros: variables con las que podemos introducir datos en las funciones
def saludar(nombre): # lo que va entre paréntesis es el parámetro
    print(f"¡Muy buenas, {nombre}!")

# Los argumentos pocicionales: van por orden de posición en la declaración de los parámetros.

# Multiples llamadas a funciones
saludar("Cristian") # lo que va entre paréntesis en la llamada es el argumento
saludar("Sebastián") # lo que va entre paréntesis en la llamada es el argumento
saludar("Julián") # lo que va entre paréntesis en la llamada es el argumento
saludar("Eluney") # lo que va entre paréntesis en la llamada es el argumento

# Multiples parámetros y argumentos en las funciones
def saludar(nombre, apellido): # lo que va entre paréntesis son los parámetros
    print(f"\n¡Muy buenas, {nombre} {apellido}!")

saludar("Cristian","Muñoz") # lo que va entre paréntesis en la llamada son los argumentos

# Argumentos clave: van en cualquier orden, ya que se indica en el propio argumento, el parámetro como clave.

def saludar(nombre, apellido): # lo que va entre paréntesis son los parámetros
    print(f"\n¡Muy buenas, {nombre} {apellido}!\n")

saludar(apellido = "Muñoz", nombre = "Cristian") # lo que va entre paréntesis en la llamada son los argumentos

# Return en las funciones: se utilizan para guardar resultados de una funcion para poder utilizarlos fuera del alcance (scope) de la función, ejemplo:

# def suma(numero1, numero2):
#     resultado = numero1 + numero2

# suma(10, 50)
# print(resultado)

# Para solucionar esto usamos el return
def suma(numero1, numero2):
    return numero1 + numero2

resultado = suma(10, 50)
print(resultado)