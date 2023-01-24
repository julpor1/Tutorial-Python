#Hacer un programa que pida 3 numeros y determine cual es mayor

num1 = int(input("Digite un valor numerico ->"))
num2 = int(input("Digite un valor numerico ->"))
num3 = int(input("Digite un valor numerico ->"))


if num1>=num2 and num1>=num3:
    print(f"El numero {num1} es el mayor")
elif num2>=num1 and num2>=num3:
    print(f"El numero {num2} es el mayor")
elif num3>=num1 and num3>=num2:
    print(f"El numero {num3} es el mayor")
