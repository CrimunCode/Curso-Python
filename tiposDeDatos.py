# Tipos de Datos en Python

## STRING  (str): Texto o cadena de caracteres

comillasSimples = "Este es un texto entre comillas simples"
comillasDobles = "Este es un texto entre comillas dobles"
comillasTriplesSimples = """Este es un texto entre comillas triples simples"""
comillasTriplesDobles = """Este es un texto entre comillas triples dobles"""

## INTEGER (int): Número Entero

numero_entero = 1

## Float (float): Número Decimal

numero_decimal = 3.14

## COMPLEJO (complex): Números Complejos, tienen una parte entera y otra parte imaginaria

numero_complejo = 5 + 2j

## LISTA (lista[]): Colección Ordenada y mutable de elementos (cada elmento tendrá un índice) y los elementos si se pueden modificar (Aray o Arreglo)

lista = [0, 1, 2, 3, 4, 5]

## TUPLA (tuple()):  Colección ordenada e inmutable de elementos (cada elemento tendrá un índice), pero los elemento no se pueden modificar

tupla = (0, 1, 2, 3, 4, 5)
tupla2 = ("a", "b", "c")

## RANGO (range): Es una secuencia de números generada dentro de un rango

rango = range(1,10)

## DICCIONARIO (dict): Es una Colección de pares clave-valor (key-value) desordenada y mutable similar a los objetos

diccionario = {
    "nombre": "Cristian",
    "edad": 40,
    "estudios": {
        "profesion": "Ingeniero en Informática",
        "duración" : "8 semstres"
    }
}

## CONJUNTO (set{}): Colección desordenada de elementos únicos y mutables

conjunto = {1,1,2,2,3}

print(conjunto)
print(lista)

## FROZENSET (frozenSet([])): Coleción desordenada de elementos únicos e inmutables

conjunto_inmutable = frozenset([1,2,2,3,3,3])

## BOOLEANOS (boll): Valor verdadero o falso

booleanoVerdadero = True
booleanoFalso = False