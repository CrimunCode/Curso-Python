# Crear una lista con elementos
lista_colores = ["Rojo", "Azul", "Verde", "Amarillo"]
lista_numeros = [5,6,8,1,69,10,54,30]

# Mostrar una lista
print(lista_colores)

# Mostrar elementos de una lista en strigs formateados
print(f"El segundo elemento de la lista es el: {lista_colores[1]}")

# Acceder a un elemento a través de su índice
print("\n", lista_colores[3],"\n")

# Acceder a un elemento a través de su índice negativo (del final hacia el primero indice)
print("\n", lista_colores[-1],"\n")

# Acceder a un caracter de un strig en una lista
print("\n", lista_colores[2][0],"\n")

# Reasignar valores a una lista
lista_colores[1] = "Naranja"
print(lista_colores, "\n")

# Insertar elementos al final de la lista
lista_colores.append("Naranja")
print("\n", lista_colores, "\n")

# Insertar elementos a un lugar especifico de la lista, desplazando al resto
lista_colores.insert(1,"Morado")
print("\n", lista_colores, "\n")

# Eliminar un elemento de una lista indicando su índice
lista_colores.pop(4)
print("\n", lista_colores, "\n")

# Eliminar un elemento de una lista indicando su valor
lista_colores.remove("Morado")
print("\n", lista_colores, "\n")

# Duplicar lista usando método copy
lista_nueva = lista_colores.copy()
print("\n", lista_nueva, "\n")

# Duplicar lista asisgnando literalmente
lista_nueva = lista_colores
print("\n", lista_nueva, "\n")

# Contar el numero de elementos de una lista
print(len(lista_numeros))

# Contar valores repetidos en listas
print(lista_colores.count("Naranja"), "\n")

# Buscar el indice de un elemento en una lista
print(lista_colores.index("Naranja"), "\n")

# Invertir el orden de los elementos en una lista
lista_colores.reverse()
print("\n", lista_colores, "\n")

# Ordenar los elementos de la lista en orden alfabético ascendente
lista_colores.sort()
print("\n", lista_colores, "\n")

# Ordenar los elementos de la lista en orden alfabético descendente
lista_colores.sort(reverse=True)
print("\n", lista_colores, "\n")

print("\n", lista_numeros, "\n")
lista_numeros.sort()
print("\n", lista_numeros, "\n")
lista_numeros.sort(reverse=True)
print("\n", lista_numeros, "\n")

# Extender una lista con otra lista
lista_colores.extend(lista_numeros)
print(lista_colores, "\n")

# Añadir un string literal a una lista, con los caracteres separados por posiciones
lista_colores.extend("Amarillo")
print(lista_colores, "\n")

# Vaciar listas
lista_colores.clear()
print("\n", lista_colores, "\n")