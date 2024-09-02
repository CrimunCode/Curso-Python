import random
def juego_adivinanza():
    # Generar un número de 1 al 100
    numero_secreto = random.randint(1,100)
    intentos = 0
    adivinado = False

    # Primeras lineas del juego, donde se da la bienvenida
    print("¡Bienvenido al juego de adivinanza de un número!")
    print("Debes adivinar un número entre el 1 y el 100")
    print("¡Intenta adivinarlo!")
    
    while not adivinado:
        # Solicitar un número del 1 al 100
        numero = input("Introduzca un número del 1 al 100: ")

        # Verificar que la entrada sea un número
        if numero.isdigit():
            numero = int(numero) # Lo estamos pasando de texto a entero
            intentos += 1

            if numero < numero_secreto:
                print(f"El número secreto es mayor a {numero}")
            elif numero > numero_secreto:
                print(f"El número secreto es menor a {numero}")
            else:
                print(f"¡Felicitaciones has ganado! \n El número {numero} es el secreto \n Lo has logrado en {intentos} intentos")
        else:
            error = str(numero)
            print(f"Por favor introduzca un número válido entre 1 y 100 ({error}, no es un número válido)")
juego_adivinanza()
