# Arg (Argumentos Pocicionales): Se puede utilizar "n" cantidad de argumentos o ningun argumento.

# Ejemplo 1
# print(*objects, sep=' ', end='\n', file=None, flush=False) # El print es una funcion que puede utilizar "n" cantidad de argumentos o ningun argumento. En este ejemplo (sacado de la literatura) el primer simbolo dentro de los parentesis del print aparece un '*' que indica que se le pueden pasar varios argumentos

# Ejemplo 2: en este ejemplo se utiliza una funcion que pueden aceptar un numero "x" indeterminado de argumentos
def prueba(*args):
    valor = 0
    print("\n")
    for i in args:
        valor += 1
        print(f"El argumento número {valor} es: {i}")

prueba("rojo", "azul", "verde", "amarillo")

# Otro ejemplo de uso de *args
def multiplicacion (*args):
    print("\n")
    for i in args:
        resultado = i * i
        print(f"El resultado de la multiplicacion es {resultado}")

multiplicacion(2,4,8,10) # Se imprimen los nmeros de los argumentos multiplicados por si mismos en cada iteración del bucle de la función


# ¿Que tipo de elementos devuelve *args? (Tupla)
def prueba(*args):
    print(f"\n",args)

prueba("rojo", "azul", "verde", "amarillo")

# **********************************************************************

# *kwargs (Key Words Arguments - Argumentos de Clave=Valor)
# Para visualizar las claves
def claves(**kwargs):
    numero = 0
    print("\n")
    for clave in kwargs.keys():
        numero +=1
        print(f"Clave {numero}: {clave}.")

claves(nombre="Javier", apellidos="Gómez", edad="27")

# Otra forma de visualizar **kwargs
def diccionario(**kwargs):
    print(f"\n",kwargs)

diccionario(nombre="Javier", apellidos="Gómez", edad="27")

# Para visualizar los valores
def claves(**kwargs):
    numero = 0
    print("\n")
    for clave in kwargs.values():
        numero +=1
        print(f"Clave {numero}: {clave}.")

claves(nombre="Javier", apellidos="Gómez", edad="27")

# Para visualizar a ambos Clave = Valor (item)
def claves(**kwargs):
    numero = 0
    print("\n")
    for clave in kwargs.items():
        numero +=1
        print(f"Clave {numero}: {clave}.")

claves(nombre="Javier", apellidos="Gómez", edad="27")

# Función predefinida Dict (Diccionario)
# Función constructora es otra forma de utilizar un diicionario en Python
dict(nombre="Cristian", apellidos="Muñoz Neira", edad="40")

# Forma normal de utilizar in diccionario en Python
{"nombre":"Cristian", "apellidos":"Muñoz Neira", "edad":"40"}

# Como usar **kwargs con diccionarios de argumento
def imprime_diccionario(**kwargs):
    print("\n")
    for elemento in kwargs.items():
        print(elemento)

usuario1 = {"nombre":"Cristian", "apellidos":"Muñoz Neira", "edad":"40"}

imprime_diccionario(**usuario1)

# Utilizar *args junto con paremetros posicionales fijos
def multiplicar(x,y,*args):
    return(x * y * args[0] * args[1])

print(f"\n",multiplicar(10,10,8,2,1))

# *args junto **kwargs y argumentos convencionales
def datos(*args, **kwargs):
    print(f"\n",args)
    print(kwargs)

usuario1 = {"nombre":"Javier", "Apellidos":"Perez", "edad":"42"}

datos(10,50,60, **usuario1)

# Los nombres de las variables args y kwargs pueden cambiar
def datos(*argumentos, **argumentos_clave):
    print(f"\n",argumentos)
    print(argumentos_clave)

usuario1 = {"nombre":"Javier", "Apellidos":"Perez", "edad":"42"}

datos(10,50,60, **usuario1)

