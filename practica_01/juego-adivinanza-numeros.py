import random
def juego_adivinanza():
    # Generar un número de 1 al 100
    numero_secreto = random.randint(1,100)
    intentos = 0
    adivinado = False

    # Primeras lineas del juego, donde se da la bienvenida
    print("\n¡Bienvenido al juego de adivinanza de un número!")
    print("Debes adivinar un número entre el 1 y el 100")
    print("¡Intenta adivinarlo!\n")
    
    while not adivinado:
        # Solicitar un número del 1 al 100
        numero = input("Introduzca un número del 1 al 100: ")

        # Verificar que la entrada sea un número
        if numero.isdigit():
            numero = int(numero) # Lo estamos pasando de texto a entero
            intentos += 1

            if numero < numero_secreto:
                print(f"El número secreto es mayor a {numero} \n")
            elif numero > numero_secreto:
                print(f"El número secreto es menor a {numero}\n")
            else:
                print("\n")
                print("*************************************************")
                print(f"¡Felicitaciones has ganado! \n El número {numero} es el secreto \n Lo has logrado en {intentos} intentos")
                print("*************************************************")
                print("\n")

                break
        else:
            error = str(numero)
            print(f"Por favor introduzca un número válido entre 1 y 100 (ERROR :({error}), NO es un número válido)")
while True:
    print("Bienvenido al menú principal")
    print("Desea jugar al Juego de Adivinar un números")
    
    respuesta = input("Para confirmar presione (s/n)").strip().lower()
    if respuesta == "s":
        juego_adivinanza()
    elif respuesta == "n":
        print("\n")
        print("*************************************************")
        print("Hata pronto")
        print("*************************************************")
        break
    else:
        error = str(respuesta)
        print(f"ERROR :({error}), NO es una opción válida")
        continue

