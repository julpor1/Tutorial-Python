#Ejercicio 8
#Hacer un programa que simule un cajero automatico con un saldo inicial de $1000 y tendra el siguiente menu de opciones:
#1.Ingresar dinero en la cuenta
#2.Retirar dinero de la cuenta
#3.Mostrar dinero disponible
#4.Salir


print("1. Ingresar dinero en la cuenta\n2. Retirar dinero de la cuenta \n3. Mostrar dinero disponible \n4. Salir")

opcion = 1
dinero = 1000
retiro_dinero = 0

while opcion != 4:
    opcion = int(input("Digite el numero de la accion que desea realizar: "))
    if opcion == 1:
        dinero_ingresado = int(input("Cuanto dinero desea ingresar en la cuenta: "))
        dinero += dinero_ingresado 
        print(f"El monto ingresado es de {dinero_ingresado} y el total de dinero en la cuenta es de {dinero}")
    elif opcion == 2:
        retiro = int(input("Cuanto dinero desea retirar: "))
        if retiro > dinero: 
            print(f"El dinero que desea retirar exede el que ya tiene en cuenta, el cual es de un valor de {dinero}")
            validar_retiro = input("Si desea retirar el dinero nuevamente escriba SI, por caso contrario NO->").upper()
            if validar_retiro == "SI":
                retiro = int(input("Cuanto dinero desea retirar: "))
                if retiro <= dinero:
                    retiro_dinero += retiro
                    input("Retiro exitoso")
                else:
                    print("Ocurrio un error")
            elif validar_retiro == "NO":
                print("adios que tenga un buen dia")
        else:
            retiro_dinero += retiro
            print("Dinero retirado con exito")
    elif opcion == 3:
        dinero -= retiro_dinero
        retiro_dinero = 0
        print(f"El dinero que usted tiene disponible es {dinero} pesos")
    elif opcion == 4:
        print("Que tenga un buen dia")
