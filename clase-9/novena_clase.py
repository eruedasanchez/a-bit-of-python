"""
Ejercicio 056

Escribir un programa que permita leer numeros que representan edades de un grupo de personas,
finalizando la lectura cuando se hayan ingresado 999 edades. 
Imprimir cuantos son menores de 18 años, cuantos tienen 18 años o mas y el promedio de edad
de ambos grupos.
Descartar valores que no representan una edad valida. (Se considera valido una edad entre 
0 y 100)
"""

import random

FIN_LECTURA = 999
MIN_EDAD = 0
MAX_EDAD = 100
DIECIOCHO = 18

menores_dieciocho = 0 
mayores_iguales_dieciocho = 0
sumador_edad_menor_dieciocho = 0
sumador_edad_mayor_igual_dieciocho = 0

for i in range(0,FIN_LECTURA):
    edad = random.randint(MIN_EDAD, MAX_EDAD)
    if edad < DIECIOCHO:
        menores_dieciocho += 1
        sumador_edad_menor_dieciocho += edad
    else:
        mayores_iguales_dieciocho += 1
        sumador_edad_mayor_igual_dieciocho += edad

print(f"La cantidad de personas menores a 18 años son {menores_dieciocho}")
print(f"El promedio de edad de las personas menores a 18 años son {sumador_edad_menor_dieciocho / menores_dieciocho}")
print(f"La cantidad de personas mayores o iguales a 18 años son {mayores_iguales_dieciocho}")
print(f"El promedio de edad de las personas menores a 18 años son {sumador_edad_mayor_igual_dieciocho / mayores_iguales_dieciocho}")

"""
Ejemplo 1

Supongamos que tenemos la siguiente secuencia de datos 1 4 5 7 8 4 0 4 7 8 5 6 9 0 1 0 1 4 5 7 8 0 -1

La secuencia termina en -1 y hay muchas subsecuencias separadas por un 0 (1 4 5 7 8 4,  4 7 8 5 6 9, 1, 1 4 5 7 8 y -1))

Mostrar la suma de cada subsecuencia y la suma total de la secuencia. Ademas, mostrar cual tiene la mayor suma y cuanto vale

"""
suma_total = 0
suma_subsecuencia = 0
numero_subsecuencia = 1
maxima_suma_subsecuencia = 0
numero_maxima_suma_subsecuencia = 1
finalizo_lista = False
CERO = 0
FINALIZAR = -1

while not finalizo_lista:
    numero = int(input("Numero: "))
    
    if numero == FINALIZAR:
        finalizo_lista = True
    else:
        print(f"Vamos a procesar la subsecuencia {numero_subsecuencia}")
        suma_subsecuencia = 0
        while numero != CERO:
            suma_subsecuencia += numero
            suma_total += numero
            numero = int(input("Numero: "))
        
        if suma_subsecuencia > maxima_suma_subsecuencia:
            maxima_suma_subsecuencia = suma_subsecuencia
            numero_maxima_suma_subsecuencia = numero_subsecuencia
        
        print(f"La suma de la subsecuencia {numero_subsecuencia} es igual a {suma_subsecuencia}")
        numero_subsecuencia += 1

print("La secuencia ha llegado a su fin")
print(f"La suma total de los elementos de la secuencia es igual a {suma_total}")
print(f"La subsecuencia con mayor suma es la subsecuencia {numero_maxima_suma_subsecuencia} y su valor es {maxima_suma_subsecuencia}")

"""
Ejemplo 2

Supongamos que tenemos la siguiente secuencia:

5 5 5 5 2 2 2 2 2 2 8 8 8 8 8 3 3 3 3 3 3 3 7 4 4 4 0

Queremos saber cuantos elementos repetidos tiene cada subsecuencia.  
"""

finalizo_lista = False
numero_subsecuencia = 1
FINALIZAR = 0

numero = int(input("Numero: "))
while not finalizo_lista:
    
    if numero == FINALIZAR:
        finalizo_lista = True
    else:
        print(f"Vamos a procesar la subsecuencia de repetidos {numero_subsecuencia}")
        numero_proceso = numero
        cant_repetidos_subsecuencia = 0
        while numero_proceso == numero:
            cant_repetidos_subsecuencia += 1
            numero = int(input("Numero: "))
        
        print(f"La cantidad de elementos repetidos que tiene la subsecuencia {numero_subsecuencia} es igual a {cant_repetidos_subsecuencia}")
        numero_subsecuencia += 1

"""
Ejemplo 2

Hacer el borde un cuadrado
"""

FILAS = 9
COLUMNAS = 9

for f in range(FILAS):
    for c in range(COLUMNAS):
        #print(f"({f},{c})")
        if f == 0 or f == FILAS - 1 or c == 0 or c == COLUMNAS - 1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
print("Letra O")

print("Ahora, vamos a dibujar la letra L")

for f in range(FILAS):
    for c in range(COLUMNAS):
        #print(f"({f},{c})")
        if c == 0 or f == FILAS - 1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
print("Letra L")

print("Ahora, vamos a dibujar la letra S")

for f in range(FILAS):
    for c in range(COLUMNAS):
        #print(f"({f},{c})")
        if (f == 0 and c < (COLUMNAS-1)/2) or (c == 0 and f < (FILAS-1)/2) or (f == (FILAS-1)/2 and c < (COLUMNAS-1)/2) or (f > (FILAS-1)/2 and c == (COLUMNAS-2)//2) or (f == FILAS-1 and c < (COLUMNAS-1)//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
print("Letra S")


print("Ahora, vamos a dibujar la letra X")

for f in range(FILAS):
    for c in range(COLUMNAS):
        #print(f"({f},{c})")
        if f == c or c == (COLUMNAS-1)-f:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
print("Letra X")
