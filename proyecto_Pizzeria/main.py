# Menú de Pizzas
p1m = { "nombre": "Hawaiana - Mediana", "precio" : 12600,
    "ingredientes": ["Churrasco", "Queso Mozarella", "Tomate","Salsa de Palta"],
}

p1f = { "nombre": "Hawaiana - Familiar", "precio" : 16600,
    "ingredientes": ["Churrasco", "Queso Mozarella", "Tomate","Salsa de Palta"],
}

p1e = { "nombre" : "Hawaiana - Extra Grande", "precio" : 20700,
    "ingredientes": ["Churrasco", "Queso Mozarella", "Tomate","Salsa de Palta"],
}

p2m = { "nombre": "Napolitana - Mediana", "precio": 10100,
    "ingredientes": ["Salsa de Ajo Parmesano", "Extra Cebolla fresca", "Queso Mozzarella", "Orégano"]
}

p2f = { "nombre": "Napolitana - Familiar", "precio": 13400,
    "ingredientes": ["Salsa de Ajo Parmesano", "Extra Cebolla fresca", "Queso Mozzarella", "Orégano"]
}

p2e = { "nombre": "Napolitana - Extra Grande", "precio": 16900,
    "ingredientes": ["Salsa de Ajo Parmesano", "Extra Cebolla fresca", "Queso Mozzarella", "Orégano"]
}

pizzas = {
    "p1m": p1m,
    "p1f": p1f,
    "p1e": p1e,
    "p2m": p2m,
    "p2f": p2f,
    "p2e": p2e,
}

# Ingredientes Extra
ie0 = { 'ingrediente': 'Sin Ingredientes Extra', 'precio': 0}
ie1 = { 'ingrediente': 'Champiñones','precio': 600 }
ie2 = { 'ingrediente': 'Aceitunas', 'precio': 400 }
ie3 = { 'ingrediente': 'Pepinillos', 'precio': 300 }
ie4 = { 'ingrediente': 'Salame', 'precio': 500 }

ingredientes_extra = {
    'ie0': ie0,
    'ie1': ie1,
    'ie2': ie2,
    'ie3': ie3,
    'ie4': ie4,
}

# print(f"\n{pizzas['p2s']['nombre']} ${pizzas['p2s']['precio']}\n")
# print(f"{pizzas['p2e']['ingredientes'][1]}")

# Variables del programa
# dinero = float(input())
# DINERO_INICIAL = dinero
total = 0
pedido = []

print("\nBienvenido a Pizzería Python\n")
print("Seleccione una Pizza del menú\n")

# print(f"1) {pizzas['p1e']['nombre']} - ${pizzas['p1e']['precio']}")

# Menu de las Pizzas
while True:
    x=1
    for pizza in pizzas:
        print(f"{x}) {pizzas[pizza]['nombre']} ; ${pizzas[pizza]['precio']}")
        x+=1
    eleccion = int(input("\nPizza seleccionada: "))

    match eleccion:
        case 1:
            print(f"\nHa elegido la Pizza {pizzas['p1m']['nombre']}\nValor: ${pizzas['p1m']['precio']}")
            total += pizzas['p1m']['precio']
            pedido.append(f"{pizzas['p1m']['nombre']} ; ${pizzas['p1m']['precio']}")
            break
        case 2:
            print(f"\nHa elegido la Pizza {pizzas['p1f']['nombre']}\nValor: ${pizzas['p1f']['precio']}")
            total += pizzas['p1f']['precio']
            pedido.append(f"{pizzas['p1f']['nombre']} ; ${pizzas['p1f']['precio']}")
            break
        case 3:
            print(f"\nHa elegido la Pizza {pizzas['p1e']['nombre']}\nValor: ${pizzas['p1e']['precio']}")
            total += pizzas['p1e']['precio']
            pedido.append(f"{pizzas['p1e']['nombre']} ; ${pizzas['p1e']['precio']}")
            break
        case 4:
            print(f"\nHa elegido la Pizza {pizzas['p2m']['nombre']}\nValor: ${pizzas['p2m']['precio']}")
            total += pizzas['p2m']['precio']
            pedido.append(f"{pizzas['p2m']['nombre']} ; ${pizzas['p2m']['precio']}")
            break
        case 5:
            print(f"\nHa elegido la Pizza {pizzas['p2f']['nombre']}\nValor: ${pizzas['p2f']['precio']}")
            total += pizzas['p2f']['precio']
            pedido.append(f"{pizzas['p2f']['nombre']} ; ${pizzas['p2f']['precio']}")
            break
        case 6:
            print(f"\nHa elegido la Pizza {pizzas['p2e']['nombre']}\nValor: ${pizzas['p2e']['precio']}")
            total += pizzas['p2e']['precio']
            pedido.append(f"{pizzas['p2e']['nombre']} ; ${pizzas['p2e']['precio']}")
            break
        case _:
            print("Opción inválida. Seleccione una opción del Menú de las Pizzas")
    
# Menu de los ingredientes extra
print("\nSelección de ingredientes Extra:\n")
while True:
    x=0
    for ingrediente in ingredientes_extra:
        print(f"{x}) {ingredientes_extra[ingrediente]['ingrediente']} ; ${ingredientes_extra[ingrediente]['precio']}")
        x+=1
    eleccion = int(input("\nIngrediente Extra: "))
    match eleccion:
        case 0:
            print("\nHa elegido no añadir ingredientes extra")
            break
        case 1:
            print(f"\nHa elegido como ingrediente extra: {ingredientes_extra['ie1']['ingrediente']} ; ${ingredientes_extra['ie1']['precio']}")
            total += ingredientes_extra['ie1']['precio']
            print(f"\nValor Pizza + Ingrediente extra: ${total}.\n")
            pedido.append(f"{ingredientes_extra['ie1']['ingrediente']} ; ${ingredientes_extra['ie1']['precio']}")
        case 2:
            print(f"\nHa elegido como ingrediente extra: {ingredientes_extra['ie2']['ingrediente']} ; ${ingredientes_extra['ie2']['precio']}")
            total += ingredientes_extra['ie2']['precio']
            print(f"\nValor Pizza + Ingrediente extra: ${total}.\n")
            pedido.append(f"{ingredientes_extra['ie2']['ingrediente']} ; ${ingredientes_extra['ie2']['precio']}")
        case 3:
            print(f"\nHa elegido como ingrediente extra: {ingredientes_extra['ie3']['ingrediente']} ; ${ingredientes_extra['ie3']['precio']}")
            total += ingredientes_extra['ie3']['precio']
            print(f"\nValor Pizza + Ingrediente extra: ${total}.\n")
            pedido.append(f"{ingredientes_extra['ie3']['ingrediente']} ; ${ingredientes_extra['ie3']['precio']}")
        case 4:
            print(f"\nHa elegido como ingrediente extra: {ingredientes_extra['ie4']['ingrediente']} ; ${ingredientes_extra['ie4']['precio']}")
            total += ingredientes_extra['ie4']['precio']
            print(f"\nValor Pizza + Ingrediente extra: ${total}.\n")
            pedido.append(f"{ingredientes_extra['ie4']['ingrediente']} ; ${ingredientes_extra['ie4']['precio']}")
        case _:
            print("Opción inválida. Seleccione una opción del Menú de Ingredientes Extra")

print("\n--- SU PEDIDO ---\n")
for i in pedido:
    print(f"-{i}.")
print(f"\nEl total a pagar es: ${total}\n")
print("\n Gracias por preferir Pizzas Python, vuelva pronto!!")