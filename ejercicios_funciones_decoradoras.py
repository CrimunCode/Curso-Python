# Ejercicio 1: Iterar listas completas e ir mostrando sus valorea en la consola.
def funcion_decoradora(funcion_parametro):
    def funcion_interna():
        print("\n->ITERADOR DE LISTAS<-")
        print("Aquí tienes todos los elementos de la lista:\n")
        funcion_parametro()
        print("La lista se recorrió con éxito.")
    return funcion_interna

colores = ['rojo', 'azul', 'verde', 'amarillo']

@funcion_decoradora
def recorre_lista():
    for i in colores:
        print(f"El valor es: {i}.")

recorre_lista()