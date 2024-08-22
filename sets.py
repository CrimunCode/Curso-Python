## set{} (Conjunto) : Colección desordenada de elementos únicos (no ordenados) y mutables* (No permite duplicados)
# * Se pueden agregar y eliminar elementos, pero los elementos no son "cambiables" ya que no tienen un orden

conjunto = {1, 1, 2, 2, 3}  # Lo elementos que estén duplicados serán omitidos
longitud = len(
    conjunto
)  # len contará la cantidad de lementos del conjunto (no tomará los duplicados)

# print(conjunto)
tipo = type(conjunto)
# print(tipo)

conjuntoConstructor = set(
    ("Este", "es", "un", "conjunto")
)  # Creamos un conjunto usando el constructor

# print(conjuntoConstructor)

# if 'conjunto' in conjuntoConstructor: # Podemos usar IN para saber si un elemento está presente
#     print("Sí está la palabra")

# if 'Python' not in conjuntoConstructor: # Podemos usar NOT IN para saber si un elemento NO está presente
#     print("Python no se encuentra en el conjunto")

# Agregar elementos a un conjunto (SET)

telefonos = {"Xiaomi", "Samsung", "Motorola"}
telefonos2 = ["Huawei", "Nokia"]  # Se puede sumar cualquier colección
telefonos.add("Iphone")  # Para agregar un elemento
telefonos.update(telefonos2)  # Con update sumamos otra colección (puede ser cualquier colección) a nuestro conjunto

# print(telefonos)

# Eliminar elementos (al no tener órden específico hay que tener mucho cuidado en el borrado)

autos = {"ford", "Peugeot", "Fiat", "Renault", "Ferrari"}

autos.remove('Ferrari') # Se borra un elemento que coincida exactamente con lo pasado por argumento (Da error si no existe)
autos.discard('Ferrari') # Se borra un elemento que coincida exactamente con lo pasado por argumento (no da error si no existe)
autos.pop() # Eliminará uno de forma aleatoria
autos.clear() # Para borrar todos los elementos presentes en el conjunto
# print(autos)

# Recorrer elementos con bucles

tecnologias = {'Python','C#','Java','Node'}

# for tecnologia in tecnologias: # De esta forma si se puede recorrer el set de elementos
#     print(tecnologia)

# for i in range(len(tecnologias)):
#     print(f"{i}.{tecnologias[i]}") # El set{} al no trabajar con indices, no se puede recorrer con indices, por lo tanto arroja error cuando se quiere hacer referencia a algún indice

# [print(tecnologia) for tecnologia in tecnologias] # Des esta otra forma también se puede recorrer el set de elementos

# Join de conjuntos: Acá entra la teoría de conjuntos de la matemática

a = {1,3,5,7,9}
b = {1,1,3,3,11}

# Union: Devuelve todos los elementos de ambos conjuntos (set) (sin modificar el conjunto original)

# c = a.union(b)
# print(c)
# c = a | b # Es lo mismo que usar unión
# print(c)

# Update: Devuelve todos los elementos de ambos conjuntos (set) (pero modifica el conjunto (set) original)

# a.update(b)
# print(a)

# c = a.update(b) # Esto no funciona
# print(c) # Muestra None
# a.union(b) # Esto no funciona
# print(a) # No se hace la unión de elementos solo muestra los elementos de a

# Intersección: va a devolver los elementos que tengan en comun ambos conjuntos (set)

# i = a.intersection(b)
# print(i)
# i2 = a & b # Esto es lo mismo que usar intersection()
# print(i2)

# a.intersection_update(b) # Intersectior_update() modifica el conjunto original (set)
# print(a)

# Comportamiento con booleanos:
booleanos = {True, False}

# booleanos_union = a.union(booleanos) # True y 1 se consideran el mismo valor, por lo cual se agregará False
# print(booleanos_union)
# booleanos_intersection = a.intersection(booleanos) # La única intersección es True ya que se considera igual a 1
# print(booleanos_intersection)

# Diferencias: devolver los elementos del primer conjunto (set) que no están presentes en el otro conjunto

# d1 = a.difference(b)
# print(d1)
# d2 = a - b # Es li mismo que usar difference
# print(d2)
# a.difference_update(b) # Difference update modifica el conjunto original (set)
# print(a)

# Diferencia simétrica: devuelve los elemento que no están prtesentes en ambos conjuntos (set)

# ds1 = a.symmetric_difference(b)
# print(ds1)
# ds2 = a ^ b # Es igual que usar symetric_difference
# print(ds2)

# a.symmetric_difference_update(b) # symetric_difference_update modifica el conjunto (set) original
# print(a)