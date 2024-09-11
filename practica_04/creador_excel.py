import pandas as pd

# Dataframe : es la información básica con el nombre d elas piezas y centímetros para poder armar el Excel.

data = {
    "Piezas:": ["Pata", "Tablero", "Puerta", "Estante", "Panel Lateral"],
    "Centimetros:": [40, 120, 60, 30, 180],
}

# Creamos en Dataframe
df = pd.DataFrame(data)

# Guardar el Dataframe en un archivo Excel

df.to_excel("muebles_medidas.xlsx", index=False)