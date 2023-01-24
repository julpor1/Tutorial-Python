#Ejercicio 4
"""Hacer un programa donde se reemplacen todos los espacios de una cadena por asteriscos y ademas cada palabra comience por mayusculas"""

palabra = input("Digite una frase: ").title()
palabra = palabra.replace(" ","*")
print(palabra)
