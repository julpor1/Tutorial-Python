#Pilas
#El concepto de pila es el ultimo en entrar es el primero en salir

pila = [1,2,3]

#Agregando elementos por el final
pila.append(4)
pila.append(5)
print(pila)

#Sacando elementos por el final
sacar = pila.pop()
print(pila)

#Mostrando el elemento que se saco
print(f'Sacando el elemento {sacar}')



