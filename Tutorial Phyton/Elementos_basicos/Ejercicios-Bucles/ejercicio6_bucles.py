#Ejercicio 6
#Hacer un programa que pida un numero por teclado y guarde en una lista su tabla de multiplicar hasta el 10.

num = int(input('Digite un numero:'))

lista = []

for i in range(1,11):
    mul = num * i
    lista.append(mul)

print(lista,end=" ")