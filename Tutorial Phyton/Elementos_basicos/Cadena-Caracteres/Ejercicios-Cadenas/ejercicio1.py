#Ejercicio 1 
"""Hacer un programa donde se debera imprimir por la consola la palabra con mas caracteres de dos palabras dadas. En el caso de
que ambas palabras tengan la misma cantidad de caracteres, deberas mostrar el mensaje Son Iguales """
palabra1 = input("Escribe una palabra: ")
palabra2 = input("Escribe una palabra: ")

if len(palabra1) > len(palabra2):
    print(palabra1)
elif len(palabra1) == len(palabra2):
    print("Son Iguales")
else:
    print(palabra2)



