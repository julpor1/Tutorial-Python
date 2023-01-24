#Ejercicio 2
#Llenar una lista con los numeros del 1 al 10, luego modificar los elementos de la lista multiplicandolos por un valor que el usuario digite.

lista = list(range(1,11))

valor = int(input("Digite un valor numerico -->"))

for i in lista:
    mul= i * valor 
    print(mul,end="-")