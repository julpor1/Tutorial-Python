#Ejercicio 2 
"""Hacer un programa para detectar si una frase introducida por el usuario finaliza con un punto "." o no. Deberas
imprimir por la consola una de las siguientes opciones; "Termina con un punto" o por el contrario "No termina con un punto." """

frase = input("Digite una frase: ")

validar = frase.endswith(".")

if validar:
    print("Termina con punto")
else:
    print("No termina con punto")