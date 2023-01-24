#Ejercicio 5
'''
Una tienda ofrece un descuento del 15% sobre el total de la compra y 
un cliente desea saber cuanto debera pagar finalmente por su compra.
'''
compra = float(input("Valor de su compra ->"))

descuento = compra * (15/100)
valor_compra = compra - descuento

print(f"El valor de la compra es {valor_compra} pesos")