import random

def obtener_palabra_secreta() -> str:
    palabras = ['python', 'javascript', 'java', 'django', 'tensorflow', 'react', 'typescript', 'git', 'flask']
    # palabras = ['git']
    return random.choice(palabras)

def mostrar_progreso(palabra_secreta, letras_adivinadas):
    adivinado = ''

    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += "_"
    return adivinado

def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 3
    juego_terminado = False

    print('¡Bienvenido al juego del ahorcado!')
    print(f'Tienes {intentos} intentos para adivinar la palabra secreta')
    print("La palabra secreta ocupa", len(palabra_secreta), "espacios :", mostrar_progreso(palabra_secreta, letras_adivinadas))

    while not juego_terminado:
        letra_ingresada = input("Escriba una letra: ").lower()

        if len(letra_ingresada) != 1 or not letra_ingresada.isalpha():
            print("\nPor favor escriba una letra válida (sólo escribir una letra)")
        elif letra_ingresada in letras_adivinadas:
            print("\nYa has utilizado esa letra, prueba con otra")
        else:
            letras_adivinadas.append(letra_ingresada)

            if letra_ingresada in palabra_secreta:
                print(f"\nMuy bien, has acertado, la letra '{letra_ingresada}' está presente en la palabra secreta")
            else:
                intentos -= 1
                print(f"\nLo siento mucho, la letra '{letra_ingresada}', no está presente en la palabra secreta")
                print(f"Te quedan {intentos} intentos")
        
        progreso_actual = mostrar_progreso(palabra_secreta, letras_adivinadas)
        print(progreso_actual)

        if "_" not in progreso_actual:
            print(f"¡Felicidades, has ganado! La palabra completa es: {palabra_secreta.upper()}")
            juego_terminado = True
    
        if intentos == 0:
            print(f"Lo sentimos mucho, se te han acabado los intentos, la palabra secreta era: {palabra_secreta.upper()}")
            break

juego_ahorcado()