#Argumentos y parametros

# def sumar(num1,num2): # Parametros: Son los datos que recibe la funcion.
#     return num1 + num2

# print(sumar(3,4)) # Argumentos: Son los datos que se envian a la funcion.
# print(sumar(num2=3,num1=4))


#Argumentos por valor o por referencia

def doblar_numero(num):
    num *= 2
    return num

n = 5
n = doblar_numero(n)
print(n)
