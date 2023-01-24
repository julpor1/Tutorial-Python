#Colas
#El concepto de colas es el primero en entrar es el primero en salir

cola = ['Julian','Mariana','Martha','Juan']

#Agregar elementos al final de la cola

cola.append("Mercedes")
cola.append("Carlos")
 
print(cola)

#Sacando elementos por el principio de la cola

sacar = cola.pop(0)
print(f"La persona que se saco fue {sacar}")
print(cola)


