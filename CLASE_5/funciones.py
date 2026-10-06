#Estructura de una funcion - (palabra clave) (nombre de la funcion) (parametros)

# def nomnbre_funcion(parametro)
def sumar(a,b):
    suma = a + b
    return suma
#invocando a las funciones
print(sumar(5,2))
#declarando en una variable
resultado = sumar(20,30)
print(resultado)

#funciones con valores por defecto de los parametros
def saludar (nombre= "pedrito" , apellido = "valdez"):
    print(f"hola {nombre} {apellido}")
saludar("Joss")

#AREA TRIANGULO
def area_triangulo (b,a):
    area = (b * a) / 2
    return area
print(area_triangulo(20,10))
    