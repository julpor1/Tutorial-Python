#Operadores Logicos
#Permite construir expresiones logicas, se obtiene como resultado booleanos.
#Operadores AND,OR,NOT 
#La Prioridad en los operadores logicos es: NOT -> AND -> OR

a=10
b=12
c=13
d=10

ejercicio = ((a > b) or (a<c)) and  ((a == c) or (a>= b))
print(ejercicio)

