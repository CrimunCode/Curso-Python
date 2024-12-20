# Importaciones
import mysql.connector

# Crear el objeto de conexión con el servidor (una variable)
conexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456",
    database = "american_rider"
)

# Crear el cursor
cursor = conexion.cursor()

# Creación de nueva base de datos con manejo de errores MySQL
'''
try:
    cursor.execute("CREATE DATABASE pruebas;")
    print("Se creó correctamente la Base de Datos")
except: # noqa: E722
    print("Ocurrió un error al crear la base de datos. Inténtelo de nuevo.")
'''
# Tipos de datos SQL
# varchar (almacena un string de más de 65.000 caracteres de longitud)
# int (almacena valores enteros muy grande más de 4.000.000.000 millones de posobilidades)
# float (para almacenar valores numéricos decimales)

# Eliminar bases de datos MySQL a traves de Python
'''
try:
    cursor.execute("DROP DATABASE pruebas;")
    print("Se eliminó correctamente la Base de Datos")
except: # noqa: E722
    print("Ocurrió un error al eliminar la base de datos. Inténtelo de nuevo.")
'''

# Crear tablas en una base de datos
try:
    cursor.execute("CREATE TABLE clientes"
    "(id INT NOT NULL AUTO_INCREMENT,"
    "nombre VARCHAR (32) NOT NULL,"
    "apellidos VARCHAR (64) NOT NULL,"
    "telefono VARCHAR (9) NOT NULL,"
    "direccion VARCHAR (256),"
    "PRIMARY KEY (id));")
    print("Se creó correctamente la tabla.")
except:  # noqa: E722
    print("Ocurrió un error al intentat crear la table. Inténtelo de nuevo.")