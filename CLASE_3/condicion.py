# una condicion 

edad = input("Edad: ")

if edad.isdigit():
    edad = int(edad)

    if edad == 0:
        print("No existes aún")

    elif edad > 0 and edad < 18:
        print("Eres menor de edad")
        
    elif edad >= 18 and edad <= 130:
        print("Eres mayor de edad")

    elif edad > 130:
        print("Ya dejaste este mundo")
 

    else:
        print("Dato inválido")
else:
    print("Se requiere un valor entero")


# multiple condicion