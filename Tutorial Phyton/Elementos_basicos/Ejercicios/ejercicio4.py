#Ejercicio 4
#Hacer un programa para ingresar el radio de un circulo y se reporte su área y la longitud de la circunferencia.
import math

radio = float(input("Radio->"))

area = math.pi * radio ** 2
longitud = 2 * math.pi * radio

#:.(numero de decimales)f se utiliza despues de un numero decimal para obtener despues del punto decimal el numero de decimales que queramos.
print(f"El area es {area:.2f}cm")
print(f"La longitud de la circunferencia es {longitud:.2f}cm")

