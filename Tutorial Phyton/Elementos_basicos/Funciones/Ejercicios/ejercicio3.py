#Ejercicio 3
"""Crear un programa que tenga una lista de clientes, cada cliente tiene su Nombre, Apellido y DNI. 
El programa tendra el siguiente menu de opciones
1. Agregar nuevo cliente
2. Mostrar todos los clientes 
3. Mostrar cliente por DNI
4. Eliminar cliente
5. Salir 

PD:Cada opcion de menu se realizara con una funcion 
"""
def agregar_cliente(clientes,nombre,apellido,dni):
    cliente = {}
    cliente["Nombre"] = nombre
    cliente["Apellido"] = apellido
    cliente["DNI"] = dni
    clientes.append(cliente)
    print(clientes)

def mostrar_clientes(clientes):
    for i in clientes:
        print(f"-----------------------\nNombre:{i['Nombre']}\nApellido:{i['Apellido']}\nDNI:{i['DNI']}\n-----------------------")
    
def mostrar_cliente(clientes,dni):
    for i in clientes:
        if i['DNI'] == dni:
             print(f"-----------------------\nNombre:{i['Nombre']}\nApellido:{i['Apellido']}\nDNI:{i['DNI']}\n-----------------------")
             return True
    return False

def eliminar_cliente(clientes,dni):
    for i in clientes:
         if i['DNI'] == dni:
            clientes.pop(clientes.index(i))
            return True
    return False
    

clientes = [] # Creamos una lista 
validar = 1
while validar != 0 :
    print("""      Menu
1. Agregar nuevo cliente
2. Mostrar todos los clientes 
3. Mostrar cliente por DNI
4. Eliminar cliente
5. Salir""")
    opcion = int(input("Digite una opcion: "))

    if opcion == 1:
        nombre = input("Digite el nombre del cliente: ")
        apellido = input("Digite el apellido del cliente: ")
        dni = input("Digite el DNI del cliente: ")
        agregar_cliente(clientes,nombre,apellido,dni)
    elif opcion == 2:
        mostrar_clientes(clientes)
    elif opcion == 3:
        dni = input("Digite el DNI del cliente: ")
        if mostrar_cliente(clientes,dni):
            print("Cliente Encontrado")
        else:
            print("Cliente no encontrado")
    elif opcion == 4:
        dni = input("Digite el DNI del cliente a eliminar: ")
        if eliminar_cliente(clientes,dni):
            print("Cliente Eliminado")
        else:
            print("Cliente No encontrado")
    elif opcion == 5:
        print("Saliendo...")
        validar = 0
    else:
        print("Opcion Incorrecta")
        








