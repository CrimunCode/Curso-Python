# Importaciones
import operaciones.sumar as sumar
import operaciones.restar as restar
import operaciones.multiplicar as multiplicar
import operaciones.dividir as dividir
import operaciones.modular as modular
import operaciones.exponenciar as exponenciar

# Titulo del programa
print("\n--- CALCULADORA ---")
print("(con funciones en Python)")

# Funciones: (se importan)

# Ciclo infinito

# Menú de la calculadora
while True:
    print("\nElija una opción:\n")
    print("1) Sumar")
    print("2) Restar")
    print("3) Multiplicar")
    print("4) Dividir")    
    print("5) Modular")    
    print("6) Exponenciar")    
    print("0) Salir")    

    # Ingreso de la opción
    eleccion = input("\nIngrese el 1º número y presione 'Enter': ")
    if eleccion.isdigit():
        eleccion = int(eleccion)
        # Confirmación de opción ingresada
        match eleccion:
            case 1: 
                print("\nMENSAJE: Ha elejido la opción 'Sumar'")
            case 2: 
                print("\nMENSAJE: Ha elejido la opción 'Restar'")
            case 3: 
                print("\nMENSAJE: Ha elejido la opción 'Multiplicar'")
            case 4: 
                print("\nMENSAJE: Ha elejido la opción 'Dividir'")
            case 5: 
                print("\nMENSAJE: Ha elejido la opción 'Modular'")
            case 6: 
                print("\nMENSAJE: Ha elejido la opción 'Exponenciar'")
            case 0: 
                print("\nMENSAJE: Saliendo de la Calculadora")
                break
            case _: 
                print("\nERROR: Opción NO válida. Selecciones un aopción del 0 al 6")
        # Se solicitan los dos números para cualquier operación que elija
        numero_1 = float(input("\nIngrese el 1º número y presione 'Enter': "))
        numero_2 = float(input("Ingrese el 2º número y presione 'Enter': "))
        # Calculos
        match eleccion:
            case 1:
                resultado = sumar.sumar(numero_1, numero_2)
                print(f"\nRESULTADO: {numero_1} + {numero_2} = {resultado}")
            case 2:
                resultado = restar.restar(numero_1, numero_2)
                print(f"\nRESULTADO: {numero_1} - {numero_2} = {resultado}")
            case 3:
                resultado = multiplicar.multiplicar(numero_1, numero_2)
                print(f"\nRESULTADO: {numero_1} * {numero_2} = {resultado}")
            case 4:
                if numero_2 == 0:
                    print("\nERROR: No se puede dividir por 0.")
                else:
                    resultado = dividir.dividir(numero_1, numero_2)
                    print(f"\nRESULTADO: {numero_1} / {numero_2} = {resultado}")
            case 5:
                resultado = modular.modular(numero_1, numero_2)
                print(f"\nRESULTADO: {numero_1} % {numero_2} = {resultado}")
            case 6:
                resultado = exponenciar.exponenciar(numero_1, numero_2)
                print(f"\nRESULTADO: {numero_1} ^ {numero_2} = {resultado}")
    else:
        error = str(eleccion)
        print(f"\nERROR: ({error}), no es una opción válida.\nPor favor ingrese una opción válida (números del 0 al 6)")