# Función: es un bloque de código autónomo que se ejecuta cuando lo llamamos, nos va a servir para atomizar y reutilizar código optimizando el mismo

# Parámetros: son la lista de variables dentro de los paréntesis
# Argumentos: son los valores que le enviamos a la función cuando es llamada
# Parámetros = variables
# def funcion(profesor, curso, femenino):
#     genero = "el profesor"
#     if femenino:
#         genero = "la profesora"
#     else:
#         genero = "le profesor"
#     print(f"El curso de {curso} lo dará {genero} {profesor}")  # Usamos Template String

    # Argumentos = valores


# funcion("Cristian", "Python desde Cero", False)
# funcion("Pedrito", "Cocina", False)
# funcion("Martina", "Manejo", True)
# funcion("Mercedes", "Guitarra", True)
# funcion("Lucho", "Aprendiendo a volar", None)

# Variable por defecto: Esto nos dará la posibilidad de NO enviar ese argumento (opcional)


# def decir_pais(pais="Chile"):
#     print(f"El nombre de mi país es: {pais}")


# decir_pais("Mexico")
# decir_pais()

# Retornar valores: una función, puede retornat valores


# def suma(a, b):
#     return a + b


# def resta(a, b):
#     return a - b


# def multiplicacion(a, b):
#     return a * b


# def division(a, b):
#     return a // b

# resultado_suma=suma(3,2)
# resultado_resta=resta(5,3)
# resultado_multiplicacion=multiplicacion(5,5)
# resultado_division=division(10,2)

# print(resultado_suma)
# print(resultado_resta)
# print(resultado_multiplicacion)
# print(resultado_division)

# Otros tipos de datos que podriamos pasar:

# lista = ["javaScript", "Python", True, 65]
# number = 33


# def usar_tipos_de_datos(lista, number):
#     print(lista)
#     print(number)


# usar_tipos_de_datos(['Hawai','Jamaica'], 1)
# usar_tipos_de_datos(lista, number)

# Argumentos Arbitrarios: mandar multiple elementos, según dependa


# def llamar_alumnos(*alumnos):
#     print(f"Mi mejor alumno es: {alumnos[0]}")
#     print(f"Mi alumna más divertida es: {alumnos[2]}")
    # print(f"Mi alumna más divertida es: {alumnos[5]}") # Hay qie tener cuidado de que esnté bien manejado para no dar erroresd


#                  0        1           2           3
# llamar_alumnos('Ricardo','Antonieta','Beatriz','Lionel')

# Argumento clave / key arguments


# def cursos(curso1, curso2, curso3):
#     print(f"El primer curso que daré será el de {curso1}")
#     print(f"El siguiente será el curso de {curso2}")
#     print(f"y para fnalizar daré eñ curso de {curso3}")


# cursos(curso3 = "Java", curso2 = "CSS", curso1 = "HTML") # Indicaremos a través de esta estructura a que parametro corresponde cada argumento

# Argumentos claves arbitrarios


# def llamar_alumno(**alumno):
#     print(
#         f'El apellido del alumno es {alumno["apellido"]}, y su nombre es {alumno["nombre"]}'
#     )


# llamar_alumno(apellido = "Perez", nombre = "Tobias", edad = 34)

# Recursividad (recursión) de una función (se puede considerar en cierta forma un bucle)

# Djemplo del factorial

# 0! = 1
# n! = n * (n1) para n > 0

def factorial(n):
    # caso base 0! = 1
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    

numero = 5
print(f'El factorial de {numero} es {factorial(numero)}')