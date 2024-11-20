# Operaciones avanzadas con Strings

# Concatenación con el operador +

p = "Programación"
f = "Fácil"

print(f"\n",p + f)
print(f"\n",p + " " + f)

# Concatenar un String con Numero (Da error)
p = "Programación"
f = 10

# print(p + " " + f) # Da error por que no se puede concatenar un String con un Integer

# Convertir el Integer a String
print(f"\n",p + " " + str(f)) 

# Concatenar con ,
print(f"\n",p,f)

# Concatenar Strings (solo para strings) con el método Join alternativa 1
p = "Programación"
f = "Fácil"

print(f"\n"," ".join([p,f,p,f]))

# Concatenar Strings (solo para strings) con el método Join alternativa 2

colores = ["Rojo", "Azul", "Verde", "Amarillo"]
separador = ";"

concatena = separador.join(colores)

print(f"\n",concatena)

# Formatear Strings con el operador %
p = "Programación"
f = "Fácil"

print("\n", "%s %s" % (p, f))

# Formatear Strings e Integers con el operador %
p = "Programación"
f = 10

print("\n", "%s %i" % (p, f))

# Formatear Strings y Floats con el operador %
p = "Programación"
f = 10.5

print("\n", "%s %f" % (p, f))

# Formatar Strings, con el método Format
p = "Programación"
f = "Fácil"

print("\n","{} {} {}".format(p,f,f))

# Foormatear string con el prefijo "f" (el de siempre)
p = "Programación"
f = "Fácil"

print("\n",f"{p} {f}")

texto = "\nEl oeste de Texas divide la frontera entre Mexico y Nuevo México. Es muy bella pero aspera, llena de cactus, en esta region se encuentran las Davis Mountains. Todo el terreno esta lleno de piedra caliza, torcidos arboles de mezquite y espinosos nopales. Para admirar la verdadera belleza desertica, visite el Parque Nacional de Big Bend, cerca de Brownsville. Es el lugar favorito para los excurcionistas, acampadores y entusiastas de las rocas. Pequeños pueblos y ranchos se encuentran a lo largo de las planicies y cañones de esta region. El area solo tiene dos estaciones, tibia y realmente caliente. La mejor epoca para visitarla es de Diciembre a Marzo cuando los dias son tibios, las noches son frescas y florecen las plantas del desierto con la humedad en el aire."

print(texto)

# Dividir Srtings en varias lineas. String conjunto ("string")
texto = ("\nEl oeste de Texas divide la frontera entre Mexico y Nuevo México. Es muy bella pero aspera,"
" llena de cactus, en esta region se encuentran las Davis Mountains. Todo el terreno esta lleno de piedra caliza," 
" torcidos arboles de mezquite y espinosos nopales. Para admirar la verdadera belleza desertica, visite el Parque" 
" Nacional de Big Bend, cerca de Brownsville. Es el lugar favorito para los excurcionistas, acampadores y "
"entusiastas de las rocas. Pequeños pueblos y ranchos se encuentran a lo largo de las planicies y cañones de esta" 
" region. El area solo tiene dos estaciones, tibia y realmente caliente. La mejor epoca para visitarla es de " 
"Diciembre a Marzo cuando los dias son tibios, las noches son frescas y florecen las plantas del desierto con la "
"humedad en el aire.") 

print(texto)

# Para mostrar el string con saltos de linea
texto = """\nEl oeste de Texas divide la frontera entre Mexico y Nuevo México. Es muy bella pero aspera,
llena de cactus, en esta region se encuentran las Davis Mountains. Todo el terreno esta lleno de piedra caliza,
torcidos arboles de mezquite y espinosos nopales. Para admirar la verdadera belleza desertica, visite el Parque
Nacional de Big Bend, cerca de Brownsville. Es el lugar favorito para los excurcionistas, acampadores y
entusiastas de las rocas. Pequeños pueblos y ranchos se encuentran a lo largo de las planicies y cañones de esta
region. El area solo tiene dos estaciones, tibia y realmente caliente. La mejor epoca para visitarla es de
Diciembre a Marzo cuando los dias son tibios, las noches son frescas y florecen las plantas del desierto con la
humedad en el aire."""

print(texto)

# Multiplicar Strings
p = "Programación"
f = "Fácil"

print("\n",p*3)
print("\n",(p+" ")*3)

# Iterar Strings en Python
pf = "Programación Fácil"

print("\n")
for letra in pf:
    print(letra)

# Iterar Strings con Range()
pf = "Programación Fácil"

print("\n")
for letra in range(len(pf)):
    print(pf[letra])

# Comprobar coincidencias en Strings en forma directa
print("\n","ción" in "Programación Fácil")

# Lo mismo pero con variables
pf = "Programación Fácil"
buscar = "xxx"

print("\n",buscar in pf)

# Saber si algo no está
print("\n",buscar not in pf)

# Generar un Diccionario a partir de un string usando el constructor dict
pf = "www.programacionfacil.org"

lista_pf = dict(enumerate(pf))

print("\n",lista_pf)

# Generar una Lista a partir de un String usando el constructor list
pf = "www.programacionfacil.org"

lista_pf = list(enumerate(pf))

print("\n",lista_pf)

# Generar una Tupla a partir de un String usando el constructor tuple
pf = "www.programacionfacil.org"

lista_pf = tuple(enumerate(pf))

print("\n",lista_pf)

# Generar un Set a partir de un String usando el constructor set
pf = "www.programacionfacil.org"

lista_pf = set(enumerate(pf))

print("\n",lista_pf)

# Comillas Simples, Dobles y Triples, dentro de un mismo String
comillas = """\n¿El cielo es de color "azul", 'celeste' o no tiene color.?"""

print(comillas)