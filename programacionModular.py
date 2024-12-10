# Programación Modular
def pow(numero1, numero2):
    return numero1 ** numero2

print(f"\n{pow(2,7)}\n")

# Alcance de variables (scope)
nombre = "Programación Fácil" # Varialbe Global

def imprimir_nombre():
    nombre = "PCMaster" # Variable local
    print(f"El nombre es {nombre}")

imprimir_nombre()

print(nombre)

# Espacio de nombres
valor = "Global"

def imprime():
    valor = "Local"
    return valor

print(valor) # Imprime Global
alcance = imprime()
print(alcance)

# Espacio de nombres
import math

calculo1 = math.pow(2,7)
print(calculo1)

def pow(numero1, numero2):
    return numero1 ** numero2

calculo2 = pow(2,7)

print(calculo2)

# Importar modulos propios

import operaciones.modulo_sumar as sm

resultado = sm.sumar(50, 50)

print(resultado)

# Importar módulos que esten dentro de carpetas