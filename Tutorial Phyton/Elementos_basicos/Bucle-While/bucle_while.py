#Bucle While 

import math

numero = int(input("Digite un numero->"))

while numero < 0:
    print("Error el numero deberia ser positivo")
    numero = int(input("Digite un numero->"))

print(f"La raiz del numero {numero} es {math.sqrt(numero):.2f}")


#Mostrar un "hola mundo" 10 veces

i = 0

while i < 10:
    print("Hola mundo")
    i += 1
