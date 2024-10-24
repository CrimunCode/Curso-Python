# Crear una lista con los siguientes valores enteros 10, 45, 55, 76
lista_numeros = [10, 10, 45, 55, 76, 10]

# Mostrar el valor 76 en la consola
print('\n', lista_numeros[3], '\n')

# Utilizar el formateo de strings (f"") para imprimir esta frase en la consola. Utiliza la lista anterior, para mostrar el 10 y el 76
print(f'El valor más pequeño en la lista es el {lista_numeros[0]}. El más grande, el {lista_numeros[3]}.\n')

# Imprimir el caracter "u" del color Azul de la lista_colores
lista_colores = ['Rojo', 'Azul', 'Verde', 'Amarillo']
print(lista_colores[1][2], '\n')

# De una lista de paises, mostrar los 2 ultimos paisas
lista_paises = ["Afghanistan","Albania","Algeria","Andorra","Angola","Anguilla","Antigua and Barbuda","Argentina","Armenia","Aruba","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bermuda","Bhutan","Bolivia","Bosnia & Herzegovina","Botswana","Brazil","British Virgin Islands","Brunei","Bulgaria","Burkina Faso","Burundi","Cambodia","Cameroon","Cape Verde","Cayman Islands","Chad","Chile","China","Colombia","Congo","Cook Islands","Costa Rica","Cote D Ivoire","Croatia","Cruise Ship","Cuba","Cyprus","Czech Republic","Denmark","Djibouti","Dominica","Dominican Republic","Ecuador","Egypt","El Salvador","Equatorial Guinea","Estonia","Ethiopia","Falkland Islands","Faroe Islands","Fiji","Finland","France","French Polynesia","French West Indies","Gabon","Gambia","Georgia","Germany","Ghana","Gibraltar","Greece","Greenland","Grenada","Guam","Guatemala","Guernsey","Guinea","Guinea Bissau","Guyana","Haiti","Honduras","Hong Kong","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Isle of Man","Israel","Italy","Jamaica","Japan","Jersey","Jordan","Kazakhstan","Kenya","Kuwait","Kyrgyz Republic","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Macau","Macedonia","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Mauritania","Mauritius","Mexico","Moldova","Monaco","Mongolia","Montenegro","Montserrat","Morocco","Mozambique","Namibia","Nepal","Netherlands","Netherlands Antilles","New Caledonia","New Zealand","Nicaragua","Niger","Nigeria","Norway","Oman","Pakistan","Palestine","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Puerto Rico","Qatar","Reunion","Romania","Russia","Rwanda","Saint Pierre & Miquelon","Samoa","San Marino","Satellite","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","South Africa","South Korea","Spain","Sri Lanka","St Kitts & Nevis","St Lucia","St Vincent","St. Lucia","Sudan","Suriname","Swaziland","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Timor L'Este","Togo","Tonga","Trinidad & Tobago","Tunisia","Turkey","Turkmenistan","Turks & Caicos","Uganda","Ukraine","United Arab Emirates","United Kingdom","Uruguay","Uzbekistan","Venezuela","Vietnam","Virgin Islands (US)","Yemen","Zambia","Zimbabwe"]
print(lista_paises[-1])
print(lista_paises[-2])

# Añadir a la lista_colores los siguientes colores en los sitios donde se pide. Con algún método de adición de elementos, no puedes editar la lista manualmante. Tienes que añadir los colores en el código en este orden: 

# Gris (antes de Rojo), 
print(lista_colores, '\n')
lista_colores.insert(0,'Gris')
print(lista_colores, '\n')

# Rosa (en ultimo lugar), 
lista_colores.append('Rosado')
print(lista_colores, '\n')

# Naranja (entre azul y verde)
lista_colores.insert(3,"Naranja")
print(lista_colores, '\n')

# De la lista_colores, eliminar los valores: (Rojo, Verde y Amarillo)

# Eliminar Rojo
lista_colores.pop(1)
print(lista_colores, '\n')

# Eliminar Verde
lista_colores.pop(3)
print(lista_colores, '\n')

# Eliminar Amarillo
lista_colores.pop(3)
print(lista_colores, '\n')

# Duplicar la lista_colores en otra
lista_nueva = lista_colores
print(lista_nueva, '\n')

# Contar cuantas veces está repetido el número 10 en la lista_numeros
print(f"El numero 10, está repetido: {lista_numeros.count(10)} veces\n")

# Emplear un método que muestre la posición del valor "Brazil" en la lista paises
print(f"La pocisión del pais Brazil es la nº: {lista_paises.index("Brazil")}\n")

# Ordenar los elementos de la lista_numeros de menor a mayor
lista_numeros.sort()
print(lista_numeros,'\n')

# Ordenar los elementos de la lista_numeros de mayor a menor
lista_numeros.sort(reverse=True)
print(lista_numeros,'\n')

# Mostrar la cantidad de paises que contiene la lista_paises
print(len(lista_paises))