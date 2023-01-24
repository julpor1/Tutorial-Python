#Ejercicio 5 
#Hacer un programa para calcular el factorial de un numero positivo 

numero = int(input("Digite un numero -->"))
valor = 1

if numero > 0:
    numero = numero + 1
    for i in range(1,numero):
        valor = valor * i 
    print(f"El factorial del numero {numero-1} es {valor}")
else:
    print("Numero negativo")