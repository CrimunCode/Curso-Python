# Menú de Pizzas
p1m = {
    "nombre": "Hawaiana - Mediano", "precio" : 12600,
    "ingredientes": ["Churrasco", "Queso Mozarella", "Tomate","Salsa de Palta"],
}

p1f = {
    "nombre": "Hawaiana - Familiar", "precio" : 16600,
    "ingredientes": ["Churrasco", "Queso Mozarella", "Tomate","Salsa de Palta"],
}

p1e = {
    "nombre" : "Hawaiana - Extra Grande", "precio" : 20700,
    "ingredientes": ["Churrasco", "Queso Mozarella", "Tomate","Salsa de Palta"],
}

p2m = {
    "nombre": "Napolitana - Mediana", "precio": 10100,
    "ingredientes": ["Salsa Garlic parmesan", "Extra Cebolla fresca", "Queso Mozzarella", "Orégano"]
}

p2f = {
    "nombre": "Napolitana - Familiar", "precio": 13400,
    "ingredientes": ["Salsa Garlic parmesan", "Extra Cebolla fresca", "Queso Mozzarella", "Orégano"]
}

p2e = {
    "nombre": "Napolitana - Extra Grande", "precio": 16900,
    "ingredientes": ["Salsa Garlic parmesan", "Extra Cebolla fresca", "Queso Mozzarella", "Orégano"]
}

pizzas = {
    "p1s": p1m,
    "p1m": p1f,
    "p1l": p1e,
    "p2s": p2m,
    "p2m": p2f,
    "p2l": p2e,
}

print(f"\n{pizzas['p2s']['nombre']} ${pizzas['p2s']['precio']}\n")
