# Tercer clase del curso de Python. Parte 2

# Tipo de dato booleano

#a = int(-1)
#x = bool(True)        # inicializacion de la variable x de tipo bool con su constructor
#b = int()             # inicializacion en 0
#print(b)

# Sentencia if
#resultado = a == -1
#resultado = a + 1     # toma este como ultimo valor 

#if resultado:         # 1 -> true, cualquier otra cosa -> false cuando se trabaja con enteros
#    print("true")
#else:
#    print("false")
#print("despues del if")

# Ejercicio 18 extraido de la ejercitacion de Flujo de Seleccion

"""
Escribir un programa que permita al usuario ingresar un número entero y luego
muestre un mensaje indicando si el número es par o impar. 
"""

numero = int(input("Bienvenido usuario. Ingrese un numero entero: "))
if not ((numero % 2) == 0):
    print("El numero", numero, "es impar")
else:
    print("El numero", numero, "es par")
