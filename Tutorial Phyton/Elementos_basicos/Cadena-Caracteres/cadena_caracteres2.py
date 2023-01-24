#Cadena de caracteres indices y slicing

cadena = "Julian"
print(cadena[0])

#Slicing
print(cadena[0:4])

#Las cadenas de texto son inmutables
# cadena[0] = "j"
# print(cadena)

#Pero hay una manera
cadena = "j" + cadena[1:]
print(cadena)

