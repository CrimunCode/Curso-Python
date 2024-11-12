#  Calcular el área de un circulo (Pi * radio * radio)

# variables
radio = float(input("\nIngrese el radio del circulo: "))

# Constantes
PI = 3.14159265359

# Función Lambda
calcular_area = lambda radio : PI * radio * radio

# Llamada a la función
area = round(calcular_area(radio), 2)

# Mostrar resultado
print(area)