#Listas

#Lista de los dias de la semana
lista = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo',[1,2,3]]
print(lista)

#Lunes
print(lista[0])

#Lunes
print(lista[-7])

#Imprimira los elementos comenzando por el elemento de la posicion 0 hasta el elemento que se encuentra antes del elemento de la posicion 5
print(lista[0:5])

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Determinar cuantos elementos posee una lista
#El metodo len me devuelve la longitud de un arreglo y de una cadena de texto
print(len(lista))

lista2 = [1,2,3,4]
#El metodo append() añade un elemento nuevo en la ultima posicion de la lista indicada.
lista2.append(6) 
print(lista2)

#El metodo insert() añade un elemento en una posicion en especifico del arreglo indicado, 
#en el primer parametro indica la posicion y el segundo parametro indica el elemento que va en esa posicion
lista2.insert(3,8)
print(lista2)

#El metodo extend() añade multiples elementos en la ultima posicion de la lista indicada.
lista2.extend(["hola","como",'estas'])
print(lista2)

#Puedo sumar dos listas y posicionar todos sus elementos en una lista nueva
lista3 = ["perro","loro",'gato']
lista4 = ["vaca","cocodrilo",'pato']

lista5 = lista3 + lista4
print(lista5)

#Verificar si un elemento se encuentra dentro la una lista con "in"

lista6 = [1,2,3,4,5,6,7,"Julian","Julian",3,4,5,2,"Julian"]
print(2 in lista6)

#Verificar en que posicion dentro de una lista se encuentra un elemento

print(lista6.index(4))
print(lista6.index(7))

#Contar cuantas veces se encuentra un elemento dentro de una lista
print(lista6.count("Julian"))

#Eliminar elementos dentro de una lista
#El metodo pop() sin ningun parametro elimina el ultimo elemento de una lista 
#pero con un parametro que especifique la posicion del elemento eliminara ese elemento

lista6.pop()
print(lista6)

lista6.pop(0)
print(lista6)

#Eliminar elemento de una lista si no conocemos su posicion

lista6.remove(3)
print(lista6)

#Eliminar toda una lista
lista6.clear()
print(lista6)

#Duplicar los elementos de una lista

lista7 = [1,2,3,4,5,6]*2
print(lista7)

#Ordenar una lista de elementos numericos del menor al mayor con el metodo sort()

lista8 = [4,2,7,1,9,-1,-2,-4]
lista8.sort()
print(lista8)
#Pasandole como parametro reverse=True al metodo sort() estamos ordenando los numeros de la lista del mayor al menor
lista8.sort(reverse=True)
print(lista8)








