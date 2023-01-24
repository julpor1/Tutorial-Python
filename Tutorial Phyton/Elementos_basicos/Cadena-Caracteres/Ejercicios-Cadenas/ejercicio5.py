#Ejercicio 5
#Hacer un programa donde se cuente cada una de la vocales en una cadena, mostrar el conteo de las apariciones de cada vocal.

palabra = input("Digite una palabra: ")
palabra = palabra.replace(" ","")
contador = 0
for i in palabra:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        contador += 1
        print(f"{i} vocal contada")

print(f"Numero de vocales {contador}")
