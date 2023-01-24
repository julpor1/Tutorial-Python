#MI EJERCICIO
operacion = input('Digite la primera letra de la operacion aritmetica que desea realizar->').upper()
num1 = int(input('Digite un valor->'))
num2 = int(input('Digite un valor->'))

if operacion == 'S':
    suma = num1 + num2
    print(f"La suma de los numeros {num1} y {num2} es {suma}")
elif operacion == 'R':
    resta = num1 - num2
    print(f"La resta de los numeros {num1} y {num2} es {resta}")
elif operacion == 'M':
    multi = num1 * num2
    print(f"La multiplicacion de los numeros {num1} y {num2} es {multi}")
elif operacion == 'D':
    division = num1 / num2
    print(f"La division de los numeros {num1} y {num2} es {division}")
else:
    print("No has escogido ninguna operacion")
