#Cajero automatico


print("1. Ingresar dinero en la cuenta\n2. Retirar dinero de la cuenta \n3. Mostrar dinero disponible \n4. Salir")

opcion = int(input("Digite el numero de la accion que desea realizar->"))
dinero = 1000

if opcion == 1:
    dinero_ingresado = float(input("Cuanto dinero desea ingresar en la cuenta"))
    dinero += dinero_ingresado 
    print(f"El monto ingresado es de {dinero}")
elif opcion == 2:
     retiro = float(input("Cuanto dinero desea retirar->"))
     if retiro > dinero: 
        print(f"El dinero que desea retirar exede el que ya tiene en cuenta, el cual es de un valor de {dinero}")
        validar_retiro = input("Si desea retirar el dinero nuevamente escriba SI, por caso contrario NO->").upper()
        if validar_retiro == "SI":
            retiro_nuevo = float(input("Cuanto dinero desea retirar->"))
            if retiro_nuevo <= dinero:
                input("Retiro exitoso")
            else:
                print("Ocurrio un error")
        elif validar_retiro == "NO":
            print("adios que tenga un buen dia")
     else:
        print("Dinero retirado con exito")
elif opcion == 3:
    print(f"El dinero que usted tiene disponible es {dinero} pesos")
elif opcion == 4:
    print("Que tenga un buen dia")
    
