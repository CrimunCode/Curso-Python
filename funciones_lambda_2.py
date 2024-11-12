#  Funciones Anónimas o Lambdas: es una sintaxis muy reducidas que sirvern para crear funciones cortas, se les dice anonimas, por que no llevan un nombre, se puede hacer solo 1 operación aritmetica (por ejemplo)

# Declaración de funciones normales
def multiplicar(numero1, numero2):
    return numero1 * numero2

# Declaración funciones lambdas
lambda numero1, numero2 : numero1 * numero2

# Como llamar a la funcion lambda (función sin nombre o anónima): asignando la funcion lambda a una variable
multiplicar = lambda numero1, numero2 : numero1 * numero2

resultado1 = multiplicar(10,7)
resultado2 = multiplicar(10,5)

print(f"\n{resultado1}")
print(f"\n{resultado2}")

# Declaración y llamada conjunta de funciones lambdas
(lambda numero1, numero2 : print(f"\n{numero1 * numero2}")) (10,8)

# El equivalente en funciones normales
def multiplicar(numero1, numero2):
    print(f"\n{numero1 * numero2}")

multiplicar(10, 8)

