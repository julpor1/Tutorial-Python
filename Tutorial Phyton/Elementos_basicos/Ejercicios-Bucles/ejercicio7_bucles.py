#Ejercicio 7 
#Estas tres funciones fueron importadas de una clase llamada random.
#1.La funcion randint(numero min,numero max) genera un numero entero aleatorio entre un rango de numeros
#2.La funcion random() genera un numero aleatorio entre 0 y 1, esta funcion no recibe parametros
#3.La funcion uniform(numero min,numero max) genera un numero decimal aleatorio entre un rango de numeros
from random import randint,random,uniform

# numero1 = random()
# numero2 = randint(1,10)
# numero3 = uniform(1,10)

# print(numero1,numero2,numero3)

aleatorio = randint(0,100)
num = 1
contador = 0

while num != 0:
    pedir = int(input("Digite un numero:"))
    if aleatorio == pedir:
        num = num - 1
    elif pedir > aleatorio:
        print("El numero escogido es mayor al numero aleatorio")
    else:
        print("El numero escogido es menor al numero aleatorio")
    contador = contador + 1

print(f"El numero aleatorio es el {aleatorio} y su numero de intentos fue {contador}")