#Funciones Integradas

#La funcion str() transforma cualquier tipo de dato a cadena de texto. 

cadena = str(10)
print(cadena)

#La funcion bin() transforma un numero a un numero binario
#Nota:Los valores binarios en paiton son mostrados como tipo cadena
binario = bin(10)
print(binario)

#La funcion hex() transforma un numero a un numero hexadecimal
hexade = hex(30)
print(hexade)

#La funcion int() me transformara un numero binario a entero
numero = int("0b1010",2)
print(numero)

numero = int("0xa",16)
print(numero)

#La funcion abs() me devuelve el valor absoluto de un numero
absoluto = abs(-12)
print(absoluto)

#La funcion round() redondea un numero decimal hacia arriba o abajo
redondeo = round(32.523)
print(redondeo)

#La funcion len() me devuelve el numero de caractares de una cadena texto
contar = len("hola")
print(contar)