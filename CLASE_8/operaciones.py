def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b    

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

print(sumar(2, 3))
print(restar(5, 2))
print(multiplicar(3, 4))
print(dividir(10, 2))
print(dividir(10, 0))