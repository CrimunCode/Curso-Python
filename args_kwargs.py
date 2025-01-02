# Arg (Argumentos): 

# print(*objects, sep=' ', end='\n', file=None, flush=False) # El print es una funcion que puede utilizar "n" cantidad de argumentos o ningun argumento. En este ejemplo (sacado de la literatura) el primer simbolo dentro de los parentesis del print aparece un '*' que indica que se le pueden pasar varios argumentos

# En este ejemplo se utiliza una funcion que pueden aceptar un numero "x" indeterminado de argumentos
def prueba(*args):
    valor = 0
    for i in args:
        valor += 1
        print(f"El argumento número {valor} es: {i}")

prueba("rojo", "azul", "verde", "amarillo")

# ¿Que tipo de elementos devuelve args? (Tupla)

def prueba(*args):
    print(args)

prueba("rojo", "azul", "verde", "amarillo")