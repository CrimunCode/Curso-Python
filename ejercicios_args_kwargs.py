# Ejercicios con *args y **kwargs
# Ejercicio 1: Corregir la funcion para sumar n cantidad de números
def sumar(*args):
    print("\n")
    print(args[0] + args[1] + args[2])

sumar(10,7,3)

# Ejercicio 2: ordegar los argumentos de la función (argumentos pocicionales, *arg)
def sumar(x, y, *args):
    print(x + y + args[0] + args[1] + args[2])
    print(args[0] + args[1] + args[2] + x + y) # El orden de impresion se puede modificar, pero el orden en la funcion será el mismo que en la llamada a la función, por eso el resultado es el mismo en ambos casos

sumar(10,20,30,40,50)

# Ejercicio 3: Crear una funcion que permita mostrar datos de un diccionario
def mostrar_datos(**datos):
    print("\n")
    claves = tuple(datos.keys())
    valores = tuple(datos.values())
    print(f"Los datos son los siguientes:\n\n{claves[0].capitalize()}   : {valores[0]}\n{claves[1].capitalize()}: {valores[1]}\n{claves[2].capitalize()}     : {valores[2]} años.")

usuario1 = {"nombre":"Cristian", "apellidos":"Muñoz Neira", "edad":"40"}
usuario2 = {"nombre":"Maritza", "apellidos":"Curilaf Neira", "edad":"38"}

mostrar_datos(**usuario1)
mostrar_datos(**usuario2)