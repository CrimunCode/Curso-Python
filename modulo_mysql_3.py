# Exportar e Importar Bases de Datos MySQL desde Python

# Módulos a utilizar
import subprocess # Módulo para ejecutar comandos externos a Python como el simbolo del sistema para ejecutar comandos de MySQL
import getpass # Módulo para ocultar la contraseña en la consola
'''
# Exportar
with open('E:/wolrd.sql','w') as out:
    subprocess.Popen(f'"C:/Program Files/MySQl/MySQL Workbench 8.0 CE/"mysqldump --user=root --password={getpass.getpass()} --databases world', shell=True, stdout=out)

'''
# Importar
subprocess.Popen(f'"C:/Program Files/MySQl/MySQL Workbench 8.0 CE/"mysql --user=root --password={getpass.getpass()} < E:/world.sql', shell=True)
# La argumento shell=True ejecuta todo el string entre comillas '' como un conjunto, como si fuera un solo comando con opciones
# El argumento stdout=out si no se especifica, se obtiene la salida en la consola y no se exportará a un archivo .sql, por lo tanto este argumentos saca el resultado del comando a un archivo con extención .sql