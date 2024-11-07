#1) Crea un bucle for que imprima los valores del 7 al 14.

print("\nEjercicio 1:")
for i in range (7,15):
    print(f"El valor del bucle es: {i}.")
print("\n")

# 2) Crea un bucle while que imprima los valores del 7 al 14.

print("Ejercicio 2:")
i = 7
while i<=14:
    print(f"El valor del bucle es: {i}.")
    i+=1
print("\n")

# 3) Crear un bucle for y luego con un bucle while que muestr uns frase como las anteriores con los valores del 0 al -5000 en decrementos de 500.

print("Ejercicio 3.1:")
for i in range(0,-5001,-500):
    print(f"El valor del bucle es: {i}")
print("\nEjeercicio 3.2")
i = 0
while i >= -5000:
    print(f"El valor del bucle es: {i}.")
    i -= 500
print("\n")

# 4) Itera con un bucle, esta lsita de países completamente.
print("Ejercicio 4")
paises = ["Afghanistan","Albania","Algeria","Andorra","Angola","Anguilla","Antigua and Barbuda","Argentina","Armenia","Aruba","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bermuda","Bhutan","Bolivia","Bosnia & Herzegovina","Botswana","Brazil","British Virgin Islands","Brunei","Bulgaria","Burkina Faso","Burundi","Cambodia","Cameroon","Cape Verde","Cayman Islands","Chad","Chile","China","Colombia","Congo","Cook Islands","Costa Rica","Cote D Ivoire","Croatia","Cruise Ship","Cuba","Cyprus","Czech Republic","Denmark","Djibouti","Dominica","Dominican Republic","Ecuador","Egypt","El Salvador","Equatorial Guinea","Estonia","Ethiopia","Falkland Islands","Faroe Islands","Fiji","Finland","France","French Polynesia","French West Indies","Gabon","Gambia","Georgia","Germany","Ghana","Gibraltar","Greece","Greenland","Grenada","Guam","Guatemala","Guernsey","Guinea","Guinea Bissau","Guyana","Haiti","Honduras","Hong Kong","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Isle of Man","Israel","Italy","Jamaica","Japan","Jersey","Jordan","Kazakhstan","Kenya","Kuwait","Kyrgyz Republic","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Macau","Macedonia","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Mauritania","Mauritius","Mexico","Moldova","Monaco","Mongolia","Montenegro","Montserrat","Morocco","Mozambique","Namibia","Nepal","Netherlands","Netherlands Antilles","New Caledonia","New Zealand","Nicaragua","Niger","Nigeria","Norway","Oman","Pakistan","Palestine","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Puerto Rico","Qatar","Reunion","Romania","Russia","Rwanda","Saint Pierre & Miquelon","Samoa","San Marino","Satellite","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","South Africa","South Korea","Spain","Sri Lanka","St Kitts & Nevis","St Lucia","St Vincent","St. Lucia","Sudan","Suriname","Swaziland","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Timor L'Este","Togo","Tonga","Trinidad & Tobago","Tunisia","Turkey","Turkmenistan","Turks & Caicos","Uganda","Ukraine","United Arab Emirates","United Kingdom","Uruguay","Uzbekistan","Venezuela","Vietnam","Virgin Islands (US)","Yemen","Zambia","Zimbabwe"]
nro_paises = len(paises)
i = 1
for pais in paises:
    print(f"Nº {i} : {pais}")
    i+=1

# 5) Iterar con un bucle la lista_numeros y mostrar todos los valores, exeptuando los valores 10 y 356.
print("\n")
lista_numeros = [10,45,356,10,10,10,46,67,45,10,10,43,10,65,10,10]
lista_numeros.sort()
for numero in lista_numeros:
    if numero == 10 or numero == 356:
        continue
    print(f"Los valores son: {numero}")
print("\n")