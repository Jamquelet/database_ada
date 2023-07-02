#variables de cada tipo de dato primitivo
entero = 7
flotante = 3.9
cadena_texto = "this is a string"
booleano = False

#concatenación de las variables
resultado = cadena_texto + ". - Este es un numero entero " + str(entero) + ". - Este es un numero flotante " + str(flotante) + ". - Este es un booleano " + str(booleano)
print ("Resultado de la concatenación:", resultado)

#Límite enteros
""" Límite de números enteros en python: Este límite esta determinado por la memoria disponible en el sistema. No hay un límite fijo predefinido. Sin embargo hay un límite práctico que está relacionado con la representación interna de los números enteros en python. En python3, los enteros se pueden representar con una precisión arbitrariamente grande, lo que significa que pueden crecer hasta ocupar toda la memoria disponible. Una variable tipo int de python puede almacenar números de -2**31 a 2**31 = -2.147.483.648 al 2.147.483.647, en plataformas de 64 bits, el rango es de -9.223.372.036.854.775.808 hasta 9.223.372.036.854.775.807"""
print("Límite de los numeros enteros en Python: pueden crecer hasta ocupar toda la memoria disponible")

#Límite flotantes 
"""Límite de los números punto flotante en python. Estos se implementan utilizando el estándar IEEE 754, que tiene límites definidos. El límite superior es aproximadamente 1.8 x 10^308, que se puede obtener mediente el acceso a la constante sys.float_info.max. Los valores que se pueden representar van desde +- 2,2250738585072020*10^-308 hasta +- 1,7976931348623157*10^308 """
print("Límite de los números punto flotante en python:", 1.8e308)

#Suma de los primeros n números pares
n = int(input("Ingresa un número entero para calcular la suma de los primeros n números pares: "))
suma = n * (n + 1)
print("Suma de los primeros", n, "números pares:", suma)

