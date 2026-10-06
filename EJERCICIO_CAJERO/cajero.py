print('\n"Bienvenido a su cajero automático"')
print("-----------------------------------")
print("  ¿Qué operación desea realizar?")
print("-----------------------------------")
print("(1) Ingresar dinero a su cuenta ")
print("(2) Retirar dinero de su cuenta ")
print("(3) Mostrar dinero disponible ")
print("(4) Salir")

saldo_inicial = 1000

while True:
    try:
        print("------------------------------------------------")
        operacion = int(input("Seleccione la operación que desea realizar: "))
        print("------------------------------------------------")
        if operacion < 1 or operacion > 4:
            print("Por favor, ingrese un número válido de operación.")
            continue
    except ValueError:
        print("------------------------------------------------")
        print("Por favor, ingrese un número válido.")
        print("------------------------------------------------")
        continue

    if operacion == 1:
        print("------------------------------------------------")
        dinero = float(input("Cuánto dinero desea ingresar: "))
        if dinero < 0:
            print("Por favor, ingrese una cantidad positiva.")
        else:
            saldo_inicial += dinero
            print("------------------------------------------------")
            print(f"Haz ingresado ${dinero}")
            print("------------------------------------------------")
            print(f"Cuenta con un saldo actual de ${saldo_inicial}")
            print("------------------------------------------------")

    elif operacion == 2:
        print("------------------------------------------------")
        retirar_dinero = float(input("Cuánto dinero desea retirar: "))
        if retirar_dinero < 0 or retirar_dinero > saldo_inicial:
            print("------------------------------------------------")
            print("Cantidad de retiro no válida. Asegúrese de tener fondos suficientes.")
        else:
            saldo_inicial -= retirar_dinero
            print("------------------------------------------------")
            print(f"Haz retirado ${retirar_dinero}")
            print("------------------------------------------------")
            print(f"Cuenta con un saldo actual de ${saldo_inicial}")

    elif operacion == 3:
        print("------------------------------------------------")
        print(f"Saldo actual: ${saldo_inicial}")

    elif operacion == 4:
        print("------------------------------------------------")
        print("Gracias por utilizar nuestro cajero, vuelva pronto!")
        print("------------------------------------------------")
        break
    print("------------------------------------------------")    
    otra_operacion = input("¿Desea realizar otra operación? (Sí/No): ").lower()
    if otra_operacion == 'no':
        print("------------------------------------------------")
        print("Gracias por utilizar nuestro cajero, vuelva pronto!")
        print("------------------------------------------------")
        break

    print("-----------------------------------")
    print("  ¿Qué operación desea realizar?")
    print("-----------------------------------")
    print("(1) Ingresar dinero a su cuenta ")
    print("(2) Retirar dinero de su cuenta ")
    print("(3) Mostrar dinero disponible ")
    print("(4) Salir")