# TUPLA: Colección (Array) que permite múltiples alementos en una sola variable. Es ordenada e inmutable de elementos (cada elemento tendrá un índice)
# indices        0             1         2        3         4        5
vehiculos = ("Bicicleta", "Motocicleta", "Auto", "Camioneta", "Avión", "Barco")
# print(vehiculos)
# longitud = len(vehiculos) # Con len, podemos saber la longitud de la tupla
# print(longitud)
# tipo = type(vehiculos) # Nos indica que es de tipo <class 'tuple'>
# print(tipo)
# tuplaConstructor = tuple(('Esta','es','una','tupla')) # Con el constructor de tupla podemos iniciar una
# print(tuplaConstructor)

# Acceso a través de índices:

# elemento1 = vehiculos[1]
# elemento2 = vehiculos[2]
# print(elemento1, elemento2)
# rango = vehiculos[3:5]
# print(rango)
# desdeInicio = vehiculos[:3]
# print(desdeInicio)
# hastaFinal = vehiculos[3:]
# print(hastaFinal)

# Truco para modificar tupla

# listaVehiculos = list(vehiculos) # En una nueva variable volcar la tupla como lista
# listaVehiculos[3] = "Camión" # Hacer el cambio que queriamos hacer
# listaVehiculos.append("Crucero") # Añadimo otro elemento al final
# vehiculos = tuple(listaVehiculos) # Asignamos a la tupla, la lista modificada convertida en tupla

# print(vehiculos)

# Desempaquetamiento: asignar cada elemento de una esrtuctura iterable a una variable distinta

(a, b, c, d, e, f) = vehiculos

# print(a)

(*terrestres, avion, barco) = (
    vehiculos  # Con el asterisco podemos agrupar parte del desempaquetamiento
)
# print(terrestres)

# Recorrer las tuplas con bucles

# for vehiculo in vehiculos:
#     print(vehiculo)

# for i in range(len(vehiculos)): # De esta forma podemos tener el indice del elemento iterable al recorrer la tupla
    # print(f"{i+1}. {vehiculos[i]}")

# [print(vehiculo) for vehiculo in vehiculos] # Este sería el shorthand para una impresión iterable de una tupla

# Join de tuplas (unir tuplas)

citricos = ('Naranja', 'Limón', 'Pomelo')
tropical = ('Papaya', 'Coco')

frutas = citricos + tropical # Con esto unimos las 2 tuplas en una nueva tupla

print(frutas)