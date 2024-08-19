# Operadores : símbolos que nos peritirán hacer operaciones sobre variables y valores

## Operadpres Aritmeticos (+,-,*,/,%,**,//)

a = 10
b = 5

suma = a + b
# print(suma)

resta = a - b
# print(resta)

multiplicacion = a * b
# print(multiplicacion)

division = a / b
# print(division) # Devuelve un flotante (con decimales)

floorDivision = a // b  # Devuelve un entero
# print(floorDivision)

resto = a % b  # Devuelve el resto de la división
# print(resto)

exponenciacion = a**b  # a como base y b como exponente 10^5=100.000
# print(exponenciacion)

## Operadores de asignación

x = 10  # El = es el operadpr de asignación más básico

x += 3  # El += le suma el valor al valor anterior
# print(x)

x -= 2  # El -= le resta el valor al valor anterior
# print(x)

x *= 2  # El *= le multiplica el valor al valor anterior
# print(x)

x /= 2  # El /= le divide el valor al valor anterior y  muestra el valor flotante
# print(x)

x //= 2  # El += le divide el valor al valor anterior y muestra el valor entero
# print(x)

x **= 2  # El += eleva valor anterior al valor indicado
# print(x)

x %= 2  # El %= muestra el resto del valor al valor anterior
# print(x)

## Operadpres de comparación (nos devolveran True o False)

num1 = 10
num2 = 5
igualdad = num1 == num2  # Devuelve True si son iguales
distintos = num1 != num2  # Devuelve True si son distintos
mayor = num1 > num2  # Devuelve True si es mayor
menor = num1 < num2  # Devuelve True si es menor
mayorIgual = num1 >= num2  # Devuelve True si es mayor o igual
menorIgual = num1 <= num2  # Devuelve True si es menor o igual

## Operadores lógicos (and, or, not)

edad = 17
tramite = (
    edad >= 18 and edad <= 65)  # Devuelve True, si se cumplen las 2 condiciones dadas
# print(tramite)

semaforo = "Verde"
cruzar = (semaforo == "Verde" or semaforo == "Amarillo")  # Devuelve True, si se cumplir al menos una de las 2 condiciones dadas
#print(cruzar)

verdad = True
#clsprint(not verdad) # NOT: niega la estructura siguiente

## Operadpres de identidad (is, is not)

nombre = "Cristian"
profesor = "Cristian"
alumno = "Pedro"

sonElMismo = nombre is profesor
#print(sonElMismo) # Devuelve True si son iguales

sonDistintos = profesor is not alumno
#print(sonDistintos) # Devuelve True si son distintos

## Operadores de Pertenencia (in, not in)

palabra = "Mundo"
texto = "Hola Mundo"
palabra2 = "Planeta"
pertenece = palabra in texto # Devuelve True si pertenece
#print(pertenece)

noPertenece = palabra2 not in texto # Devuelve true si no pertenece
print(noPertenece)