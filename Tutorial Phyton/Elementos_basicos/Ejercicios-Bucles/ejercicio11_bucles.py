#Ejercicio 11
'''Hacer un programa que simule una agenda de contactos. Crear un diccionario donde la clave sea el nombre del usuario y el valor sea el telefono
el programa tendra el siguiente menu de opciones

1.Nuevo Contacto
2.Borrar Contacto
3.Ver Contactos Existentes
4.Salir
'''


print("       MENU\n1.Nuevo Contacto\n2.Borrar Contacto\n3.Ver Contactos Existentes\n4.Salir")

diccionario = {}
c = 1

while c != 0:
    c = int(input("Digite la opcion que desea realizar: "))
    if c == 1:
        clave = input("Digite el nombre del contacto nuevo: ")
        valor = input("Digite el numero del contacto nuevo: ")
        diccionario[clave] = valor
    elif c == 2:
        clave = input("Digite el nombre del contacto a eliminar: ")
        if clave in diccionario:
            del(diccionario[clave])
            print("Contacto Eliminado")
        else:
            print("Contacto Inexistente")
    elif c == 3:
        for clave,valor in diccionario.items():
            print(f"{clave} - {valor}")
    elif c == 4:
        print("Salir")
        c = 0



