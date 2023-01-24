#Ejercicio 3
"""Hacer un programa que determine si una palabra o frase es palindroma. Una cadena palindroma se lee igual de izquierda a
derecha que de derecha a izquierda"""
cadena = input("Digite una frase: ")

#Primero quitamos los espacios en blanco de la cadena

cadena = cadena.replace(" ","")

#Invertimos la cadena
cadena2 =  cadena[::-1]

if cadena == cadena2:
    print("Es palindroma")
else:
    print("No es palindroma")

#MI FORMA DE RESOLVERLO 

# separar = ".".join(cadena)
# lista = separar.split(".")
# lista2 = []
# contador = 0

# for i in lista:
#     contador -= 1
#     lista2.append(lista[contador])
    
# cadena2 = ""
# for i in lista2:
#     cadena2 +=i

# if cadena == cadena2:
#     print("Es Palindroma")
# else:
#     print("No es palindroma")


