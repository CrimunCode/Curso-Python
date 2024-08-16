# Tipos de datos Numéricos

## INTEGER (int): Número Entero
numero_entero = 1

## Float (float): Número Decimal
numero_decimal = 3.14

## COMPLEJO (complex): Números Complejos, tienen una parte entera y otra parte imaginaria
numero_complejo = 5 + 2j

## TYPE (type()) Método, para ver el tipo de dato de una variable

print(numero_entero)
print(type(numero_entero))

print(numero_decimal)
print(type(numero_decimal))

print(numero_complejo)
print(type(numero_complejo))


## CASTEAR (Transformar una variable de un tipo de dato a otro tipo de dato numérico)

decimal_desde_entero    = float(numero_entero)
entero_desde_decimal    = int(numero_decimal)
complejo_desde_entero   = complex(numero_entero)
complejo_desde_decimal  = complex(numero_decimal)

print(decimal_desde_entero)
print(entero_desde_decimal)
print(complejo_desde_entero)
print(complejo_desde_decimal)

# NÚMEROS RANDOM

import random

aleatorio = random.randrange(1,10) # El número de stop, no se incluye
aleatorio_par = random.randrange(2,11,2) # Números pares del 2 al 10 (incluido el 10)
aleatorio_impar = random.randrange(1,10,2) # Números impares del 1 al 9 (incluido el 9)

print(aleatorio)
print(aleatorio_par)
print(aleatorio_impar)
