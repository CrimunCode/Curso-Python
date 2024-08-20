# LISTAS: estructura de datos (array) que permite almacenar múltiples elementos en una sola variable, es ordenada (podemos ingresar a sus elementos por medio del indice) y es mutable

# indices     0         1       2      3
frutas = ['Naranja','Manzana','Pera','Pera'] # Permite duplicados
numeros = [0,1,2,3,4,5]
booleanos = [True, False, True]
listaMixta = ['Naranja',1,True]

# tipo = type(listaMixta) 
# print(listaMixta)
# print(tipo) # Esto nos indica que tipo de dao es: "List"

listaDesdeCostructor = list(('Manzana','2','True')) # Hay qie utilizar el constructor list y doble paréntesis (())

# print(listaDesdeCostructor)

# Acceder a los datos

naranja = frutas[0]
# print(naranja)
rangoLista = frutas[1:3] # Desde el indice 1(Manzana) hasta el indice 3 (no inclusive)
# print(rangoLista)
desdeComienzo = frutas[:2] # Desde el comienzo hasta el 2 (no incluido)
# print(desdeComienzo)
hastaFinal = frutas[2:] # Desde el indice 2 hasta el final
# print(hastaFinal)

# Verificar si existe un elemento

# if "Manzana" in frutas: # utilizando la palabra "in" podemos saber si está presente
#     print('Si está incluido')

# Como cambiar los datos de la lista

# indice          0        1        2       3       4
tecnologias = ['Python','Django','Flask','ReactPy','Pandas']

# tecnologias[1] = 'TensorFlow' # Reemplazar el elemento de un indice particular
tecnologias[2:4] = ['NumPy','Scrapy'] # Reemplazar una parte de la lista

# Agregar elementos a una lista
tecnologias.insert(2,'Flask') # Insertart uns nuevo elemento en un índice específico
tecnologias.append('TensorFlow') # Agregamos un elemento nuevo al final de la lista
frontend = ('Angular','React','Vue') # Tupla de elementos
# diccionario = {"nombre": "Cristian"} # Diccionario de elementos
tecnologias.extend(frontend) # Agregamos una tupla a la lista (fusión)
# tecnologias.extend(diccionario) # Solo se añada el atributo clave (no el valor) no sirve
# print(tecnologias)

# Eliminar elementos
listaABorrar = ['Python','Django','Flask','ReactPy','Pandas']

tecnologias.remove('Vue') # Se remueve el elmento qur coincida con lo que ponemos como argumento
tecnologias.pop() # Podemos eliminar el ultimo elemento, si no se especifica un indice
tecnologias.pop(7) # Podemos eliminar un elemento en especifico indcando su indice
# del tecnologias[6] # Usando la palabra del podemo especificar el elemento a eliminar
listaABorrar.clear() # Para vaciar la lista
# print(listaABorrar)

# Recorrer listas

# for tecnologia in tecnologias:
#     print(tecnologia)

# for i in range(len(tecnologias)): # De esta forma podemos tener el indice del elemento iterable al recorrer la lista
#     print(f"{i+1}. {tecnologias[i]}")

# Shorthand para mostrar una lista

# [print(tecnologia) for tecnologia in tecnologias] # Este sería el shorthand para una impresión iterable

# Ejemplo Práctico

# listaConY = []

# for tecnologia in tecnologias:
#     if "y" in tecnologia:
#         listaConY.append(tecnologia)

# print(listaConY)

# lo que se agrega en mayúsculas |        el buble             | la condición
lista2ConY = [tecnologia.upper() for tecnologia in tecnologias if "y" in tecnologia] # Shorthand del ejemplo anterior

# print(lista2ConY)

# Ordenamiento de una lista

# print(tecnologias)
# tecnologias.reverse() # Ordena exactamente al revés tal cual estaba la lista
# print(tecnologias)
# tecnologias.sort() # En caso de no especificarn ordena alfabéticamente en forma ascendente
# print(tecnologias)
# tecnologias.sort(reverse=True) # Ordena alfabéticamente en forma descendente
# print(tecnologias)

# numeros = [8,2,5,3,7,6,4,1]
# print(numeros)
# numeros.reverse() # Ordena exactamente al revés tal cual estaba la lista 
# print(numeros)
# numeros.sort() # Ordena en forma ascendente
# print(numeros)
# numeros.sort(reverse=True) # Ordena en forma descendente
# print(numeros)

# Copiar una lista

meses = ['Enero','Febrero','Marzo','Abril','Mayo']
meses2 = ['Junio', 'Julio', 'Agosto', 'Septiembre']

copiaMeses = meses.copy()
copiaMeses2 = list(meses) # Usando el constructor

# print(copiaMeses,copiaMeses2)

joinMeses = meses + meses2 # Podemos juntar las listan (Join) utilizando el símbolo +
print(joinMeses)
meses.extend(meses2)
print(meses)