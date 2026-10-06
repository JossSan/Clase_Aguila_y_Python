# #Tipos de datos
# edad = 20
# precio = 10.5
# estudia = True
# print(type(edad))
# print(type(precio))
# print(type(estudia))

# #Variables con datos dinamicos
# pais = input("Ingrese su pais: ")
# print(type(pais))

# #Interpolacion
# print(f"Mi pais es: {pais} ")

# #Ingresando numeros
# date1 = int(input("Ingrese un numero: "))
# print(f"Mi dato numerico es: {date1}")

# date2 = input("Ingrese su primer numero: ")
# date3 = input("Ingrese su segundo numero: ")
# sum = int(date2) + int(date3)
# print(sum)

#Operaciones matematicas- datos de entrada y salida

a = input("Ingrese un numero: ")
b = input("Ingrese un numero: ")

# procesando datos:
sumar = a + b
restar = a - b
division_exacta = a / b
division_entera = a // b
multiplicacion = a * b
potencia = a ** b #a = 10 y b = 2 --> 10² 
resto_division = a % b

#  salida de datos
print(f"La suma es: {sumar} ")
print(f"La resta es: {restar} ")
print(f"La división exacta es: {division_exacta} ")
print(f"La división entera es: {division_entera} ")
print(f"La multiplicación es: {multiplicacion} ")
print(f"La potencia es: {potencia} ")
print(f"El resto de la divisón: {resto_division} ")