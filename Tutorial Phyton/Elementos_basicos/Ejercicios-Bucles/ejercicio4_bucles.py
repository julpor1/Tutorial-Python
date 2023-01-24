#Ejercicio 4 
#Hacer un programa para sumar numeros pares dentro de un rango

sumar = 0

for i in range(2,31):
    if (i % 2) == 0:
         sumar = sumar + i

print(sumar)
