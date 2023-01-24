#Ejercicio 2
"""Hacer un programa que pida la anchura y altura de un rectangulo y con ayuda de una funcion lo dibuje con * """

ancho = int(input("Digite el valor del ancho: "))
alto = int(input("Digite el valor del alto: "))

def rectangulo(ancho,alto):
    for i in range(1,alto + 1 ):
        for i in range(1,ancho + 1):
            print("*",end=" ")
        print()


rectangulo(ancho,alto)
