# DICCIONARIO (dict): Es una Colección de pares clave-valor (key-value) desordenada y mutable similar a los objetos


diccionario = {
    "nombre": "Cristian",
    "canal": "@crimun",
    "tecnologias": ["Python", "Javascript"],
    "edad": 40,
    "direccion": { "calle": "Av. Guillermo Ulriksen","nro": "1781","ciudad": "La Serena", },
}

# print(diccionario)
# tipo = type(diccionario) # Nos indica el tipo de dato <class 'dict'>
# print(tipo)
# longitud = len(diccionario) # Nos indica la cantidad de claves-valor que tien el diccionario
# print(longitud)
# constructorDiccionario = dict(nombre = "crimun", youtube = "@crimun") # Se puede crear con constructor, sin parentesis dobles a deferencia de otras estructuras (tupla, listas, set) y los atributos claves van sin comillas a diferencia de otras estructuras (tupla, listas, set)
# print(constructorDiccionario)

## Como acceder a cada propiedad del diccionario

# nombre = diccionario['nombre']
# canal = diccionario['canal']
# tecnologias = diccionario['tecnologias']
# edad = diccionario['edad']
# direccion = diccionario['direccion']
# print(nombre)
# print(canal)
# print(tecnologias)
# print(edad)
# print(direccion)

# canal = diccionario.get("canal")
# print(canal)
# keys = diccionario.keys() # El tipo de dato que devuelve se llama <class 'dict_keys'>
# print(keys)
# values = diccionario.values() # El tipo de dato que devuelve se llama <class 'dict_values'>
# print(values)
# items = diccionario.items() # Nos devuelve tuplas de clave-valor en una lista // <class 'dict_items'>
# print(items)

# if "tecnologias" in diccionario: # Con esto podemos comprobar si una key existe pero no un valor
    # print('Si, existe esta key')

## Cambio de valores en un diccionario

# diccionario['tecnologias'] = ['Java', 'NodeJS']
# print(diccionario)
# diccionario.update({"direccion": { "calle": "Calle Raul Bitran","nro": "1700","ciudad": "La Serena", }})
# print(diccionario)

## Agregar items:

# diccionario['profesion'] = 'Programador'
# print(diccionario)

# diccionario.update({'comida favorita': 'Guiso de Mote'})
# print(diccionario)

## Eliminar items

# diccionario.pop('comida favorita') # Eliminar un elemento puntual
# print(diccionario)

# diccionario.popitem() # Eliminará el último item agregado usar con precaución
# print(diccionario)

# del diccionario["edad"]
# print(diccionario)

# diccionario.clear() # Esto deja vacio el diccionario
# print(diccionario)


## Bucles (loops) para diccionarios:

curso_python = {
    'nombre': 'Python desde cero',
    'duracion': '7 hrs.',
    'dificultad': 'media',
}

# for key in curso_python: # EL bucle for común hará un recorrrido de las keys
#     print(f"{key.upper()}: {curso_python[key]}")

# for x in curso_python.values(): # Este bucle, recorrerá solo los valores
#     print(x)

# for k,v in curso_python.items(): # Desempaquetamos la tupla de cada uno de los elementos de la lista que devuelve items
#     print(f"{k.upper()}: {v.capitalize()}")

# Copias de diccionarios:

# copia = curso_python.copy() # Crea una copia exacta, pero está apuntando a otra variable que se encuentra en otro espacio de memoria
# print(copia)

# copia2 = dict(curso_python) # Crea una copia exacta usando el método constructor
# print(copia2)

## Diccionarios anidados:

hijo1 = {
    'nombre': 'Pedro',
    'edad': 5,
}
hijo2 = {
    'nombre': 'Alan',
    'edad': 7,
}
hijo3 = {
    'nombre': 'Enzo',
    'edad': 9,
}

familia = {
    'hijo1': hijo1,
    'hijo2': hijo2,
    'hijo3': hijo3,
}

# print(familia['hijo1']['nombre'])
# nombreHijo1 = familia['hijo1']['nombre']
# print(nombreHijo1)

for x,obj in familia.items():
        print(f'\n {x.capitalize()} \n')
        for y in obj:
                print(f'{y.capitalize()}:{obj[y]}')

