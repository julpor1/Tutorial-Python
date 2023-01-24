#Ejercicio 1
def conversion(valor,opciones):
    if opciones == 1:
        valor2 = (1*valor)/4700
        print(f"Moneda Local: ${valor} = Dolar: ${valor2}")
    elif opciones == 2:
        valor2 = (4700*valor)/1
        print(f"Dolar: ${valor} = Moneda Local: ${valor2}")


print("""       Opciones 
1.Moneda Local A Dolar
2.Dolar A Moneda Local""")
opciones = int(input("Digite la opcion que desea realizar: "))

if opciones == 1:
    dato = int(input("Digite el valor de la moneda local: "))
    conversion(dato,opciones)
elif opciones == 2:
    dato = int(input("Digite el valor en dolares: "))
    conversion(dato,opciones)
else:
    print("Opcion Incorrecta")




   
        



