#Tuplas
#Las tuplas son un tipo de lista pero inmutable esto quiere decir que no podemos ni añadir,
#modificar o eliminar algun elemento, solo se pueden buscar elementos

tupla = (4,"Hola",True,2,2.23)

print(tupla[2])
print(tupla[-2])
print(tupla[0:4])
print("Hola" in tupla)
print(tupla.index(True))
print(tupla.count(4))
print(len(tupla))

#Transformar una tupla a lista
#El metodo list() transforma una tupla a lista
lista = list(tupla)

print(lista)

#Transformar una lista a tupla
lista2 = [1,2,3,"hola","h3434"]
tupla2 = tuple(lista2)
print(tupla2)

