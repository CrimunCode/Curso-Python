# Diccionarios
microsoft_office = {
    "word"          : "Procesador de texto",
    "excel"         : "Hojas de cálculo",
    "powerpoint"    : "Presentador de diapositiva",
}

# Mostrar todo el diccionario pero en formato original
print(f"\n{microsoft_office}")

# Mostrar el valor (value) de un elemento del diccionario, por medio de su clave
print(f"\n{microsoft_office["word"]}")

# Mostrar el valor (value) de un elemento del diccionario, por medio de su clave
diccionario = {
    1 : "Valor 1",
    2 : "Valor 2",
    3 : "Valor 3",
}
print(f"\n{diccionario[3]}")

# Añadir nuevos elementos al diccionario
microsoft_office["outlook"] = "Cliente de correos"
print(f"\n{microsoft_office["outlook"]}")

# Declarar un diccionario vacio
diccionario_vacio = {}
print(f"\n{diccionario_vacio}")

# Editar elementos ya existentes en el diccionario
print(f"\n{microsoft_office['excel']}")

microsoft_office = {
    "word"          : "Procesador de texto",
    "excel"         : "Hojas de cálculo",
    "powerpoint"    : "Presentador de diapositiva",
}

microsoft_office["excel"] = "Planillas u Hojas de cálculo"

print(f"\n{microsoft_office['excel']}\n")

# Iterar altributos claves del diccionario
for programa in microsoft_office:
    print(f"-{programa.capitalize()}")

print("\n")

# Iterar valores del diccionario
for programa in microsoft_office:
    print(f"-{programa.capitalize()} : {microsoft_office[programa]}")

# Set o conjunto no tienen orden, como los diccionario o listas, tampoco tienen atributos clave, se muestran en forma aleatoria y no muestra elementos repetidos
animales = {"perro","iguana","gato","pitón","chimpancé"}
print(f"\n{animales}")

# añadimos perro 2 veces
animales = {"perro","iguana","gato","pitón","chimpancé","perro"}
print(f"\n{animales}")

# La lista si muestr los elementos repetidos
animales = ["perro","iguana","gato","pitón","chimpancé","perro"]
print(f"\n{animales}")


