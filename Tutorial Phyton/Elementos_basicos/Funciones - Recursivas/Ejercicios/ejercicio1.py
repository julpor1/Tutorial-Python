#Ejercicio 1
#Desarrollar un programa para calcular el factorial de un numero con ayuda de una funcion recursiva.

def factorial(num):
    if num>0:
        resultado = num * factorial(num - 1)
    else:
        resultado = 1

    return resultado


valor = factorial(5)
print(valor)

        


