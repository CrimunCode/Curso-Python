# Ejercicios POO 1
# Clase y atributos de clase
class Vehiculo():
    color = "sin color"
    modelo = "sin modelo"
    marca = "sin marca"

# Metodos
def arrancar(self):
    print(f"El vehiculo {self.marca} ha arrancado")

def detener(self):
    print(f"El vehiculo {self.marca} se ha detenido")

# Instancias del objeto
vehiculo_01 = Vehiculo()

# Llamados a métodos del objeto
arrancar(vehiculo_01)
detener(vehiculo_01)

print (vehiculo_01.color)