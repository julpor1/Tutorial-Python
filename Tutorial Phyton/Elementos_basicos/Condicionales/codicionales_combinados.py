#Codicionales anidados

edad = int(input("Digite su edad->"))

if edad > 0 and edad < 100:
    print("Edad correcta")
    if edad >= 18:
        print("Eres mayor de edad")
    elif edad < 18:
        print("Eres menor de edad")
else:
    print("Edad incorrecta")
