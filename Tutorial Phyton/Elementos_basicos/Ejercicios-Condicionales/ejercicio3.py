#Hacer un programa que pida un caracter y me indique si es una vocal o no
#El metodo lower() transforma una cadena de texto a minuscula

letra = input("Digite un caracter->").lower()

if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
    print("Es una vocal")
else:
    print("No es una vocal") 

    