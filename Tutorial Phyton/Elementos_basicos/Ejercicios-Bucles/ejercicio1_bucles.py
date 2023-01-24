#Ejercicio 1
'''Llenar una lista con los numeros del 1 al 50, luego mostrar la lista con un bucle for, los elementos deben mostrarse
de la siguiente forma 1-2-3-4-...-50'''

lista = []
i = 1

#Agregamos los 50 elementos a la lista con ayuda de un bucle while
while i <= 50:
    lista.append(i)
    i = i + 1

#Mostramos por consola todos los 50 elementos con ayuda de un bucle for
for i in lista:
    print(i,end="-")

#OTRA FORMA DE RESOLVER ESTE PROBLEMA
#El metodo range() crea una coleccion ficticia de datos numericos
#El metodo list() transforma esta coleccion en una lista

lista2 = list(range(1,51))

for i in lista2:
    print(i,end="-")