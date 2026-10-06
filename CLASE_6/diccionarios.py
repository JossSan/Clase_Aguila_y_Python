#clave : valor 

persona = {
    "Nombre":"joss",
    "Ciudad":"Lima",
    "Pais":"Perú",
    "Contraseña":"1234"
}
#CRUD con diccionarios
print(persona)
#mostrar el valor de una clave 
print(persona["Nombre"])
print(persona["Contraseña"])

#agregar datos al diccionario
persona["Edad"] = 20
print(persona)

#modificar un dato del diccionario
persona["Ciudad"] = "Cuzco"
print(persona)

#eliminar elementos del diccionario
del persona["Contraseña"]
print(persona)

#para que te avise que se elimino
eliminar = persona.pop("Edad")
print(f"Se elimino: {eliminar}")
print(f"Actualizado: {persona}")

#recorrer un diccionario (solo claves)
for x in persona:
    print(x)

#valor de las claves
for x in persona.values():
    print(x)
    
#mostra clave y valor
for x,y in persona.items():
    print(f"{x} -- {y}")
    
#Para saber si una clave existe o no
dato = input("Ingrese la clave a buscar: ")
buscador = persona.get(dato, "No existe")
print(buscador)