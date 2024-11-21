# 1) Utilizar el método join() para concatenar los valores de la lista

frase = ["Estoy", "aprendiendo", "Python", "con", "el", "curso", "de", "100", "días", "de", "Programación", "Fácil."]

print("\n"," ".join(frase))

# 2) Iterar la lista de colores y presentarla en la consola, con el método format(). Utiliza las constantes para presentarla como en la imagen de ejemplo. Además. los colores tendrán la primera letra en mayúscula. Ej.: 
'''
- Rojo.
- Azul.
- Verde.
- Amarillo.
'''
# Lista variable
colores = ["rojo", "azul", "verde", "amarillo"]

# Constantes
GUION = "-"
PUNTO = "."

print("\n")
for color in colores:
    print("{}{}{}\n".format(GUION,color.capitalize(),PUNTO))

# 3) A partir de estas variables, saca un un solo print() y utilizando el operador de concatenación % una frase exactamente igual que la del resultado:

numero_1 = 10
numero_2 = 34.50
resultado = numero_1 * numero_2

'''
La multiplicación de 10 * 34.500000 da como resultado: 345.000000.
'''

print("\n", "La multiplicción de %i * %.1f da como resultado: %.1f." % (numero_1, numero_2, resultado)) # %.x donde x = al número de decimales que queremos mostrar

# 4) Con el siguiente código, crea un sistema que sepa contar las coincidencias de una letra introducida en la consola.

texto = "Muy lejos, más allá de las montañas de palabras, alejados de los países de las vocales y las consonantes, viven los textos simulados. Viven aislados en casas de letras, en la costa de la semántica, un gran océano de lenguas. Un riachuelo llamado Pons fluye por su pueblo y los abastece con las normas necesarias. Hablamos de un país paraisomático en el que a uno le caen pedazos de frases asadas en la boca. Ni siquiera los todopoderosos signos de puntuación dominan a los textos simulados; una vida, se puede decir, poco ortográfica. Pero un buen día, una pequeña línea de texto simulado, llamada Lorem Ipsum, decidió aventurarse y salir al vasto mundo de la gramática. El gran Oxmox le desanconsejó hacerlo, ya que esas tierras estaban llenas de comas malvadas, signos de interrogación salvajes y  puntos y coma traicioneros, pero el texto simulado no se dejó atemorizar.Empacó sus siete versales, enfundó su inicial en el cinturón y se puso en camino. Cuando ya había escalado las primeras colinas de las montañas cursivas, se dio media vuelta para dirigir su mirada por última vez, hacia su ciudad natal Letralandia, el encabezamiento del pueblo Alfabeto y el subtítulo de su propia calle, la calle del renglón. Una pregunta retórica se le pasó por la mente y le puso melancólico, pero enseguida reemprendió su marcha. De nuevo en camino, se encontró con una copia. La copia advirtió al pequeño texto simulado de que en el lugar del que ella venía, la habían reescrito miles de veces y que todo lo que había quedado de su original era la palabra 'y', así que más le valía al pequeño texto simulado volver a su país, donde estaría mucho más seguro. Pero nada de lo dicho por la copia pudo convencerlo, de manera que al cabo de poco tiempo, unos pérfidos redactores publicitarios lo encontraron y emborracharon con Longe y Parole para llevárselo después a su agencia, donde abusaron de él para sus proyectos, una y otra vez. Y si aún no lo han reescrito, lo siguen utilizando hasta ahora."
print("\n",texto)
while True:
    letra_ingresada = (input("\nEscriba una letra para buscar en el texto: ").lower())
    contador = 0
    if letra_ingresada.isalpha():
        for letra in texto:
            if letra_ingresada in letra:
                contador += 1
        print(f'\nSe contó {contador} veces la letra "{letra_ingresada}" en el texto.')
        break
    else:
        error = str(letra_ingresada)
        print(f"\nERROR: ({error}) no es una letra válida.Ingrese una letra de la A a la Z.")