#Conjuntos
#En un conjunto se almacenan datos UNICOS y desordenados
#Para crear conjuntos se necesita primero inicializar una variable con la funcion set() y luego esa misma variable inicializarla denuevo con {}

conjunto = set()
#Nota:Dentro de los conjuntos no puede ir otro tipo de colecciones
conjunto = {1,2,3,4,"hola"}

#EL metodo add() agrega un nuevo elemento al conjunto
conjunto.add(5)

#El metodo discard() eliminar un elemento del conjunto
#El metodo discard() recibe el elemento a eliminar
conjunto.discard(2)

#El metodo clear() elimina todo un conjunto
# conjunto.clear()
print(conjunto)

print(3 in conjunto )
print(3 not in conjunto )

#----------------------------------------------------------------------------------------------------------------------
#PARTE 2 CONJUNTOS
#Error del video -> Para crear un conjunto no es necesario la funcion set() si al 
#conjunto se le asignan los elementos al momento. Los elementos de un conjunto deben estar separados por comas(pyton se da cuenta que es un conjunto)
a = {1,2,3}
b = {5,4,3}

#Para unir dos conjuntos se utiliza el signo " | "
c = a | b

#Para hacer un intercepcion entre conjuntos se utiliza el signo " & "
#La intercepcion son los elementos que se encuentran tanto en un elemento como en otro.

i = a & b

#Para la diferencia de conjuntos se utiliza el signo " - "
#La diferencia de conjuntos son los elementos que se encuentran en un un conjunto y no se encuentran en el otro conjunto.

d = a - b 
db = b - a 

#Para la diferencia simetrica se utiliza el signo " ^ "
#La diferencia simetrica entre conjuntos son los elementos que se 
#encuentran en "a" pero no en "b" y los elementos que se encuentran en "b" pero no en "a"

ds = a ^ b


print(c)
print(i)
print(d)
print(db)
print(ds)

#Saber si un conjunto es subconjunto de otro

conjuntoa = {1,2,3,4}
conjuntob = {1,2,3,4,5,6,7,8,9}

print(conjuntoa.issubset(conjuntob))

#Saber si un conjunto es el superconjunto de otro

print(conjuntob.issuperset(conjuntoa))

#Saber si un conjunto es disconexo a otro
#El termino disconexo entre conjuntos significa que no comparten elementos en comun

print(conjuntoa.isdisjoint(conjuntob))

#Transformar a inmutable un conjunto

conjuntoc = frozenset({56,3,23,12})












