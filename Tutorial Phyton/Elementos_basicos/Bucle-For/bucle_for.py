#Bucle For
#El bucle for consta de una variable iteradora y una coleccion de elementos.
#La variable iteradora se encargara de recorrer cada elemento dentro de la coleccion. Por cada elemento recorrido ejecutara el bucle.
#La variable iteradora tambien toma el valor del elemento que esta recorriendo.

#Primera Forma
# for i in [1,2,3,4,5,6]:
#     print(f"El elemento que se esta recorriendo es: {i}")

# #Segunda Forma
# c = [1,2,3,4,5,6]
# for i in c:
#     print(f"El elemento que se esta recorriendo es: {i}")

#Con Diccionarios

# diccionario = {"Julian":20,"Mariana":11,"Liam":19,"Meiby":18}

# for i in diccionario:
#     print(f"El elemento que se esta recorriendo es: {i} = {diccionario[i]}")


# diccionario2 = {"Nombre":"Julian","Apellido":"Acevedo","Genero":"Masculino","Edad":20}

# for clave,valor in diccionario2.items():
#     print(f"{clave}:{valor}")

#Con Cadenas
#Con "end" hago que cuando el print muestre lo que vale "i" no de un salto de linea sino de un espacio.
cadena = "Julian"

for i in cadena:
    print(f"{i}",end=" ")


