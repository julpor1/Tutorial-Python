#Condicionales

#Condicional if

numero = int(input("Digite un numero:"))

#Todo el codigo que este espaciado despues del condicionales if, pertenecera a ese condicional. 
# if numero >= 0 : 
#     print("El numero es positivo")
# else:
#     print("El numero es negativo")

# print("Fin del programa")

#Condicional elif

if numero > 0:
    print("El numero es positivo")
elif numero == 0:
    print("El numero es cero")
else:
    print("El numero es negativo")

print("Fin del programa")