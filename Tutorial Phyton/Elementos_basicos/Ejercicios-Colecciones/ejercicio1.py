#Ejercicio 1
#Escriba un programa donde tenga una lista y que, a continuacion, elimine los elementos repetidos, por ultimo mostrar la lista

lista = [1,2,3,"Julian",2,2,3,3,1,"Julian"]

#El metodo set() puede transformar una lista o una tupla a conjunto.
conjunto = set(lista)
print(conjunto)

#Tranformo nuevamente el conjunto a lista para optener una lista con elementos unicos
lista2 = list(conjunto)
print(lista2)


