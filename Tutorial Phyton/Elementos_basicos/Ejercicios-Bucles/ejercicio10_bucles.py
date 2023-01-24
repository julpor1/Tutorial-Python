#Ejercicio 10
#Hacer un programa que pida una cadena por teclado, luego meta los caracteres en una lista sin repetir caracteres

cadena = input("Digite una cadena: ")
lista = []

for i in cadena:
    if i != " ":
        lista.append(i)

conjunto = set(lista)
lista = list(conjunto)

print(lista)