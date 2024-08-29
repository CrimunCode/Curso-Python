# Función: es un bloque de código autónomo que se ejecuta cuando lo llamamos, nos va a servir para atomizar y reutilizar código optimizando el mismo

# Parámetros: son la lista de variables dentro de los paréntesis
# Argumentos: son los valores que le enviamos a la función cuando es llamada
                # Parámetros = variables
def funcion(profesor, curso, femenino):
    genero = "el profesor"
    if femenino:
        genero = "la profesora"
    else:
        genero = "le profesor"
    print(f"El curso de {curso} lo dará {genero} {profesor}") # Usamos Template String

            # Argumentos = valores
funcion("Cristian", "Python desde Cero", False)
funcion("Pedrito", "Cocina", False)
funcion("Martina", "Manejo", True)
funcion("Mercedes", "Guitarra", True)
funcion("Lucho", "Aprendiendo a volar", None)
