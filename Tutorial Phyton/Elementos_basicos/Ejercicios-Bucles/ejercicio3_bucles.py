#Ejercicio 3 

'''Pide numeros y metelos en una lista, cuando el usuario meta un 0 ya dejaremos de insertar. Por ultimo, muestra los numeros ordenados
de menor a mayor'''
lista = []
valor = int(input("Digite un valor numerico-->"))

while valor != 0:
    lista.append(valor)
    valor = int(input("Digite un valor numerico-->"))

#La funcion sort() ordena los datos numericos de una lista del menor al mayor
lista.sort()
#En este caso el metodo set() transforma una lista a conjunto
conjunto = set(lista) 
#En este caso el metodo list() transforma un conjunto a lista
lista = list(conjunto)
print(lista)