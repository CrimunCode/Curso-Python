# Variables
# Son creadas cuando se les asigna un valor
# Es caseSensitive diferencia mayusculas de minisculas

# Nombres admitidos de variables
# Sólo pueden contener caracteres alfanumericos y guines bajos (A-Z a-z 0-9 _)

mivariable = "texto"
_mivariable = "otro texto"
MiOtraVariable = """
otro texto más
"""
_MiOtraVariableMás = """
otro texto con comillas simples triples
"""

print(mivariable)
print(_mivariable)
print(MiOtraVariable)
print(_MiOtraVariableMás)

# una variable no puede iniciar con un número

# No se pueden utilizar palabras reservadas (keywords)

# Convenciones de escritura de variables

# Camel Case
camelCase = "Comienza con minúscula y cada palabera siguiente comenzará con mayúscula"

# Pacal Case
PacalCase = "Comienza con mayúscula y cada palabera siguiente comenzará con mayúscula"

# Snake Case
snake_case = (
    "Se usan las palabras con minúscula y cada palabera es separada con guiones bajos"
)

# Multiasignación

x, y, z = 1, 2, 3

print(x)
print(y)
print(z)

# Multi asignación desde colecciones

frutas = ["Naranja", "Manzana", "Pera"]
n, m, p = frutas

print(n, m, p)

# Reasignación : en Python las varialbes se reservan en lugares de memoria diferentes, por lo tanto no se afectan las otras variables. Ver ejemplos

a = b = c = "Gus"
print(a, b, c)
b = "Cris"  # Aqui se reserva otro espacio de memoria y se reasigna sólo la variable b.
print(a, b, c)

# Concatenación

txt = "Curso"
txt2 = "de"
txt3 = "Python"

print(txt + " " + txt2 + " " + txt3)  # Concatenando variables de tipo string + espacios vacios
print(txt, txt2, txt3)  # Imprimiendo variables de tipo string

# Scope (alcance) de Variables globales y locales 

variableGlobal = "Variable Global: estará disponible para todo el programa"

def funcionScope():
    variableLocal = "Variable Local: estará disponible dentro del alcance de la función"
    variableGlobal = "Variable Global: que se adopta un valor dentro de la función, pero luego recupera su valor fuera de la función, como variable global"
    global variableGlobal2
    variableGlobal2 = "Variable Global: que que no cambia su valor dentro o fuera de una función ya que se declara dentro de la función como una variable global su valor fuera de la función, se mantiene como variable global"
    print(variableLocal)
    print(variableGlobal)

funcionScope()
print(variableGlobal)
print(variableGlobal2)