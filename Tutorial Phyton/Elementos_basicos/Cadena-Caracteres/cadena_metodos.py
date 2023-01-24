#Cadena de caracteres metodos

#El metodo upper() transforma a MAYUSCULA una cadena de caracteres
cadena = "hola mundo".upper()
print(cadena)

#El metodo lower() transforma a minuscula una cadena de caracteres
cadena = "HOLA MUNDO".lower()
print(cadena)

#El metodo capitalize() transforma a MAYUSCULA la primera letra de una cadena de caracteres
cadena = "hola mundo".capitalize()
print(cadena)

#El metodo title() transforma a MAYUSCULA la primera letra de cada palabra de una cadena de caracteres
cadena = "hola mundo".title()
print(cadena)

#El metodo count() me devuelve un numero entero indicando cuantas veces se encuentra el caracter o palabra pasado como parametro
cadena = "hola mundo".count("h")
print(cadena)

#El metodo find() me devuelve la primera coincidencia(posicion) que encuentre en la cadena de caracteres
cadena = "hola mundo hola mundo".find("mundo")
print(cadena)

#El metodo rfind() me devuelve la ultima coincidencia(posicion) que encuentre en la cadena de caracteres
cadena = "hola mundo hola mundo".rfind("mundo")
print(cadena)

#El metodo isdigit() comprueba si una cadena esta compuesta unicamente por valores numericos.
#Devuelve True si es verdad o False si es falso
cadena = "1000a".isdigit()
print(cadena)

#El metodo isalpha() comprueba si una cadena esta compuesta unicamente por caracteres alfabeticos.
#Devuelve True si es verdad o False si es falso
cadena = "asdd12".isalpha()
print(cadena)

#El metodo isalnum() comprueba si una cadena esta compuesta tanto por caracteres numericos como caracteres alfabeticos
cadena = "sasas1212=".isalnum()
print(cadena)

#El metodo islower() comprueba y devuelve True si toda la cadena de caracteres esta en minuscula
cadena = "hola=".islower()
print(cadena)

#El metodo isupper() comprueba y devuelve True si toda la cadena de caracteres esta en MAYUSCULA
cadena = "HOLA=".isupper()
print(cadena)

#El metodo isspace() comprueba y devuelve True si solo si en la cadena de texto existen espacios en blanco
cadena = "   ".isspace()
print(cadena)

#El metodo startswith() valida el caracter o palabra con el que comience la cadena de caracteres.
cadena = "hola mundo".startswith("hola")
print(cadena)


#El metodo endswith() valida el caracter o palabra con el que termine la cadena de caracteres.
cadena = "hola mundo".endswith("mundo")
print(cadena)

#El metodo split() transforma una cadena de caracteres a lista tomando los elementos por espacios, comas, guiones, puntos, etc.
cadena = "hola mundo mundo".split()
print(cadena)

#El metodo join() separa cada caracter de la cadena que tiene como parametro tomando como referencia lo que tenga la primera cadena.
cadena = "-".join("holaatodos")
print(cadena)

#El metodo strip() elimina los espacios innecesarios o cualquier tipo de simbolo de una cadena de caracteres
cadena = "     hola     ".strip()
print(cadena)

#El metodo replace() remplaza 
cadena = "hola a todos".replace("todos","mundo")
print(cadena)

















