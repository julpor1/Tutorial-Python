#Funciones sin retorno de valor
#Para crear funciones se necesita de la palabra especial "def"

def sumar():
     num1 = 1 
     num2 = 3
     suma = num1 + num2
     print(suma)

#Llamar funcion
sumar()

#Funciones con parametro

def saludar(nombre):
    print(f"Hola {nombre}")

saludar("Julian")


def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f"{numero}*{i} = {numero*i}")

tabla_multiplicar(2)

#Funciones en las cuales un unico parametro puede recibir multiples argumentos

def multiples_argumentos(*parametro):
    for valor in parametro:
        print(valor)


multiples_argumentos(2,4,5,6,7,1,"Hola a todos")











