#listas en python 
frutas = ["uva","platano","manzana"]
#mostrar un dato de la lista
print(frutas[1])
#modificando datos de la lista
frutas[0] = "naranja"
print(frutas)

#crear un nuevo dato en la lista
frutas.append("papaya")
print(frutas)

#para eliminar un dato 
frutas.pop(2)
print(frutas)

#agregar muchos datos
frutas.extend(["durazno", "fresa", "mango"])
print(frutas)

#agregar e insertar un dato en base a un indice
frutas.insert(0,"chirimoya")
print(frutas)

#para eliminar en base a su nombre del dato
frutas.remove("durazno")
print(frutas)

#para limpiar toda la lista
#frutas.clear()
#print(frutas)

#para especificar a que indice pertener en base a su nombre 
buscador = frutas.index("fresa")
print(buscador)

#frutas.extend(["mango", "fresa", "fresa"])
#print(frutas)

#contador de datos repetidos en una lista
#contador = frutas.count("fresa")
#print(contador)

#orden ascendente
frutas.sort()
print(frutas)

#orden descendente ordenando la lista
frutas.sort(reverse=True)
print(frutas)
#para eliminar datos repetidos
#set

#revirtiendo lista sin importar el orden
#frutas.reverse()
#print(frutas)


#para recorrer una lista
for i in frutas:
    print(f"Bienvenido mi estimado: {i}")