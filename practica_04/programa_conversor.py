import pandas as pd

def cm_a_pulgadas(cm):
    return cm / 2.54

# Leer el archivo excel:
df = pd.read_excel("muebles_medidas.xlsx")

# Añadir una columna al DataFrame que sea de pulgadas y se rellene con el cálculo de cm / 2.54

df["Pulgadas:"] = df["Centimetros:"].apply(cm_a_pulgadas)

df.to_excel("mueble_medidas_convertidas.xlsx", index=False)

print("Conversion completada y grardada en un nuevo archivo llamado 'mueble_medidas_convertidas.xlsx'")