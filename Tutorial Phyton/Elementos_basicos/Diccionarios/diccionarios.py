#Diccionarios
#Los diccionarios almacenan datos desordenos que se crean con una clave y un valor

diccionario = {"color":"rojo","edad":20,"sangre":"A+"}

print(diccionario["color"])
print(diccionario["edad"])
print(diccionario["sangre"])

#Agregar elementos a un diccionario

diccionario["peso"] = "70kg"
print(diccionario)

#Modificar el valor de un elemento

diccionario['color'] = "azul"
print(diccionario)

#Eliminar un elemento
#Para eliminar un elemento de un diccionario se utiliza la funcion del()
del(diccionario['edad'])
print(diccionario)

#-----------------------------------------------------------------------------------------------------------------------------------
#Dentro de un diccionario pueden existir tanto listas,tuplas,conjuntos y otros diccionarios.

diccionario2 = {"Julian":{"edad":20,"genero":"Masculino"}}
print(diccionario2["Julian"])

#PARTE 2 VIDEO

equipo = {10:"Messi",7:"Cristiano",11:"Cuadrado",1:"Ospina"}

print(equipo.items())

print(equipo)
print(equipo[10])
print(equipo[7])
print(equipo[11])

#El metodo get() en los diccionarios me muestra el valor que se le asigna a una clave, en el caso que la clave no exista en ese diccionario;
#get() mostrara lo que se encuentre en el segundo parametro
print(equipo.get(10,'NO SE ENCONTRO NINGUN VALOR'))
print(equipo.get(22,'NO SE ENCONTRO NINGUN VALOR'))

#Validar si una clave existe en un diccionario

print(7 in equipo)
print(12 in equipo)

#Mostrar de un diccionario unicamente las claves

print(equipo.keys())

#Mostrar de un diccionario unicamente los valores

print(equipo.values())

#Mostrar la longitud de un diccionario
print(len(equipo))

#Eliminar todos los elementos de un diccionario
print(equipo.clear())










