# Exportar e Importar Bases de Datos MySQL desde Python

# Módulos a utilizar
import subprocess
import getpass
'''
# Exportar
with open('E:/wolrd.sql','w') as out:
    subprocess.Popen(f'"C:/Program Files/MySQl/MySQL Workbench 8.0 CE/"mysqldump --user=root --password={getpass.getpass()} --databases world', shell=True, stdout=out)

'''
# Importar
subprocess.Popen(f'"C:/Program Files/MySQl/MySQL Workbench 8.0 CE/"mysql --user=root --password={getpass.getpass()} < E:/world.sql', shell=True)

