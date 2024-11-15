# Crear una clase vacia llamada motocicleta

class Motocicleta():
    # Atributos de clase
    estado = "nueva"
    motor = False

    
    # Métodos: 
    # Método __init__ (Atributos de instancia)
    def __init__(self, color, patente, combustible_litros, nro_ruedas, marca, modelo, fecha_fabricacion, velocidad_punta, peso, combustible_maximo):
        self.color = color
        self.patente = patente
        self.combustible_litros = combustible_litros
        self.nro_ruedas = nro_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_punta = velocidad_punta
        self.peso = peso
        self.combustible_maximo = combustible_maximo
    
    def arrancar(self):
        if self.motor:
            print("\nEl motor ya estaba en marcha")
        else:
            self.motor = True
            print("\nEl motor ha arrancado")

    def detener(self):
        if self.motor:
            self.motor = False
            print("\nSe deteniene el motor")
        else:
            print("\nEl motor ya estaba detenido")

    def consultar_precio(self):
        print(f"\nEl precio de la motocicleta {self.marca}, modelo {self.modelo}, es de: ${self.precio}.")

    def comprobar_deposito(self):
        print(f"\n--->REPORTE DE COMBUSTIBLE DE LA MOTOCICLETA {self.marca} {self.modelo}<---")
        print(f"El depósito tiene {self.combustible_litros} litros.")
        print(f"La capacidad máxima del estanque de combustible es de {self.combustible_maximo} litros.")
        print(f"Faltan {self.combustible_maximo - self.combustible_litros} litros.")
        print("--->FIN DEL REPORTE<---\n")

    def recargar_combustible(self):
        while True:
            self.litros_recarga = (input(f"\nIngrese la cantidad de litros que desee recargar para la motocicleta {self.marca} {self.modelo}: "))
            if self.litros_recarga.isdigit():
                self.litros_recarga = float(self.litros_recarga)
                if self.combustible_litros + self.litros_recarga <= self.combustible_maximo:
                    print("Recarga Exitosa.")
                    print(f"Se han recargado {self.litros_recarga} litros.")
                    self.combustible_litros += self.litros_recarga
                    print(f"El depósito tiene {self.combustible_litros} litros de combustible")
                    break
                else:
                    print("\nERROR: No has suficiente capacidad para tanto combustible.")
            else:
                error = str(self.litros_recarga)
                print(f"\nERROR: ({error}) no es un valor válido, favor ingrese un valor numerico nuevamente.")

# Intancias
motocicleta_Honda_01 = Motocicleta("Negra", "JDKW-93", 10, 2, "Honda", "Navi", "20/11/2024", 220, 400,17)
motocicleta_Yamaha_01 = Motocicleta(
    marca = "Yamaha", 
    modelo = "Samurai", 
    peso = 250,
    velocidad_punta = 250, 
    fecha_fabricacion = "03/03/2024", 
    color = "Negra", 
    combustible_litros = 0, 
    combustible_maximo= 20, 
    patente = "HBJI-75", 
    nro_ruedas = 2, 
)

# Asignar atributo nuevo, fuera de la clase (despues de haber creado o instanciado un objeto en concreto)
motocicleta_Honda_01.precio  = 499990
motocicleta_Yamaha_01.precio  = 399990

# Llamado a funciones
motocicleta_Honda_01.arrancar()
motocicleta_Yamaha_01.arrancar()
motocicleta_Honda_01.detener()
motocicleta_Yamaha_01.detener()
motocicleta_Yamaha_01.consultar_precio()
motocicleta_Honda_01.consultar_precio()
motocicleta_Honda_01.comprobar_deposito()
motocicleta_Yamaha_01.comprobar_deposito()
motocicleta_Honda_01.recargar_combustible()
motocicleta_Honda_01.comprobar_deposito()


# Mostrar manualmente
# print(f"\nEl precio de la motocicleta {motocicleta_Honda_01.marca}, modelo {motocicleta_Honda_01.modelo}, es de: ${motocicleta_Honda_01.precio}.\n")
# print(f"\nMarca: {motocicleta_Yamaha_01.marca}\nModelo: {motocicleta_Yamaha_01.modelo}\nColor: {motocicleta_Yamaha_01.color}")

