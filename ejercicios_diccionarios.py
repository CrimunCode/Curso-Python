colores = {
    1 : "rojo",
    2 : "azul",
    3 : "verde",
    4 : "amarillo",
}
print("\n")
for color in colores:
    print(f"Color Nº{color}: {colores[color].capitalize()}")

print("\n")
colores[5] = "naranjo"
for color in colores:
    print(f"Color Nº{color}: {colores[color].capitalize()}")