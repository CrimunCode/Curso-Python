# Importaciones
import mysql.connector

# Crear el objeto (una variable) de conexión con el servidor
conexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456"
)

# Crear un cursor, con el cual podremos movernos por las bases de datos (es una forma de hacer que se puedan procesar los resultados de las consultas que haremos en el servidor)
cursor = conexion.cursor()

# Prueba de conexión, para consultar y mostrar todas las bases de datos del servidor
cursor.execute("SHOW DATABASES")

# Crear un bucle para (leer y mostrar las bases de datos en el servidor) que itere el listado a mostrar
i = 0
for bd in cursor: # type: ignore (para ignorar algunor falsos positivos en cuanto a errores de programación)
    i+=1
    print(f"{i}) {bd}")