#Ejercicio 9 
'''Hacer un programa donde el usuario ingrese una frase, se le devolvera la misma frase pero sin espacios en blanco y ademas un contador
de cuantos caracteres tiene la frase (sin contar los espacios en blanco)

Ejemplo:
            Frase:Hola que tal?
            Frase Final:Holaquetal?
            N° Caracteres:11'''


frase = input("Digite una frase: ")
frase2 = ""
for i in frase:
    if i != " ":
        frase2 = frase2 + i 

contador = 0
for i in frase2:
    contador+= 1


print(f"La frase: {frase}\nLa frase final: {frase2} \nEl N° de caracteres es: {contador}")
