# CONDICIONALES (if, elif, else) : son las estructuras que permite tomar un flujo u otro según una condición
"""
a = 5
b = 9
c = 7

if a > b:
    print(f"{a} es mayor que {b}")
elif c > b:
    print(f"{c} es matoy que {b}")
else:
    print(f"{a} es menor que {b} y {c} es menor que {b}")
""" 

""" 
edad = 61

if edad >= 18 and edad <= 60:
    print("Bienvenido al Boliche")
else:
    if edad < 18:
        print("No tienes edad suficiente para ingresar al Boliche")
    else:
        print("Este boliche solo admite personas hasta los 60 años")
""" 
## SHORTHANDS

a = 5
b = 2

#if a > b: print(f"{a} es mayor que {b}") # Shorthand del IF solo

# Ejecución si es verdadero | condición | Ejecución si es falso
print("B es mayor que A") if b >a else print("A es mayor que B") # Shorthand de IF + ELSE

