# STRING  (str): Texto o cadena de caracteres

comillasSimples = "Este es un texto entre comillas simples"
comillasDobles = "Este es un texto entre comillas dobles"
comillasTriplesSimples = """Este es un texto entre comillas triples simples"""
comillasTriplesDobles = """Este es un texto entre comillas triples dobles"""

texto = "Este es un curso de Python"

carater = texto[5]  # Para seleccionar un caracter por indice

# print(carater)

# len() Length : Para saber el largo de un string
largo = len(texto)
# print(largo)

# in: para saber si está incluido algo en el texto
# print("Python" in texto)

# not in : con la palabra reservada not podemos negar y pedir un resultado negativo
# print("Python" not in texto)

# slice() : Cortar una parte del texto

# print(texto[11:16]) # Se imprime el fragmento que vaya desde el indice 10 al 16 (no incluido)
# print(texto[:16]) # Se imprime el fragmento que vaya desde el comienzo al indice 16 (no incluido)
# print(texto[16:]) # Se imprime el fragmento que vaya desde el indice 16 hasta el final
# print(texto[-4:]) # Se imprimirá el fragmento que vaya desde 4 indices antes del final hasta el final
# print(texto[:-22]) # Se imprimirá el fragmento desde el comienzo hasta 37 caracteres antes del final

# Modificadores de texto (Mayusculas, minusculas)
textoConEspacios = "     Hola Mundo    "

# upper()
mayusculas = texto.upper()  # Texto a mayusculas

# lower()
minusculas = texto.lower()  # Texto a minusculas
# print(texto)
# print(mayusculas)
# print(minusculas)

# strip()
textoSinEspacios = (textoConEspacios.strip())  # Elimina espacios al comienzo y al final del string
# print(textoSinEspacios)

reemplazo = texto.replace("Python", "PYTHON")  # Reemplaza Python por PYTHON
# print(texto)
# print(reemplazo)

# Métodos más usados
textoAModificar = "Este es UN texto A MODIFICAR"

# capitalize()
capitalizado = textoAModificar.capitalize() # Sólo quedará la primera letra  con mayúscula
# print(capitalizado)

# startswith()
comienzaCon = textoAModificar.startswith("Este") # Busca en el comienzo la palabra que se entrerga
# print(comienzaCon)

# endswith()
terminaCon = textoAModificar.endswith("MODIFICAR")
#print(terminaCon)

# title()
titulo = textoAModificar.title() # Pone en mayúscula el comienzo de cada palabra
# print(titulo)

# count()
contador = textoAModificar.count("A") # Cuenta cuantas veces aparece la letra "e" en el texto
# print(contador)

# find()
buscaIndice = textoAModificar.find("texto") # Nos devuelve el índice donde comienza la palabra buscada
# print(buscaIndice)

# split()
textoConComas = "Santiago,La Serena,Coquimbo,Chiloé"
separarPorComas = textoConComas.split(",")  # Separará el texto por comas y nos devolvera una lista (array) de elementos sin coma

# print(separarPorComas)

# Concatenar
a = "Hola"
b = "Mundo"
c = a + " " + b
# print(c)

# F-Strings (Template Strings)

nombre = "Ricardo"
edad = 5
txt = f"{nombre} tiene {edad:.1f} años"  # nos permite utilizar variables en texto y formatearlas
# print(txt)

resultado = f"El resultado de 5 x 5 es {5*5}"
# print(resultado)

# Escapes \ (Backslash - barra invertida)
escape = "Mi país favorito es \"Lituania\" por que me dió la ciudadanía Europea"
# print(escape)
directorio = "El directorio de este curso está ubicado en: E:\\Escritorio\\Curso Python\\Contenidos\\"
# print(directorio)

saltoDeLinea = "Esto es un \nSalto de Linea"
# print(saltoDeLinea)