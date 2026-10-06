#Ciclo while
# ejemplo ciclo infinito

#while True:
# print()

correo = input("Ingrese su correo: ")

while correo != "joss@gmail.com":
    print("Correo invalido, vuelva a intentarlo")
    correo = input("Ingrese su correo: ")
print("Correo valido")