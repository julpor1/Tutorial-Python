#Ejercicio 2
#Escriba un programa que tenga dos lista y que, a continuacion, cree las siguientes listas(en las que no debe haber repeticiones)
#1.Lista de elementos que aparecen en las dos listas
#2.Lista de elementos que aparecen en la primera lista, pero no en la segunda.
#3.Lista de elementos que aparecen en la segunda lista, pero no en la primera.
#4.Lista de elementos que aparecen en ambas listas.

#1.Punto
lista1 = [1,2,3,4,5,"Julian",'Acevedo',2,3,4,"Acevedo"]
lista2 = [1,2,2,8,7,"Robinson",'Acevedo',2,3,4,"Parra"]


conjunto1 = set(lista1)
conjunto2 = set(lista2)


#2.Punto

lista3 = conjunto1 - conjunto2
print(lista3)
lista3 = list(lista3)
print(lista3)

#3.Punto

lista4 = conjunto2 - conjunto1
lista4 = list(lista4)
print(lista4)

#4.Punto

intercepcion = conjunto1 & conjunto2
print(intercepcion)

listaIntercepcion = list(intercepcion)
print(listaIntercepcion)






