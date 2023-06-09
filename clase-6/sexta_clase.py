"""
Ejercicio 029

Escribir un programa que permita ingresar las notas de los dos parciales de un alumno 
e indicar si promociono, aprobo o debe recuperar. Si el valor de la nota no esta entre
1 y 10 debe informar un error.
Se promociona cuando las notas de ambos parciales son mayores o iguales a 7.
Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4.
Se debe recuperar cuando al menos una de las notas en menor a 4.  
"""

CERO = 0
CUATRO = 4
SIETE = 7
DIEZ = 10

nota_primer_parcial = int(input("Ingrese la nota del primer parcial: "))
nota_segundo_parcial = int(input("Ingrese la nota del segundo parcial: "))

hay_alguna_nota_invalida = not (CERO <= nota_primer_parcial <= DIEZ and CERO <= nota_segundo_parcial <= DIEZ)   
promociona = (nota_primer_parcial >= SIETE) and (nota_segundo_parcial >= SIETE)
aprueba = (nota_primer_parcial >= CUATRO) and (nota_segundo_parcial >= CUATRO)   
recupera = (nota_primer_parcial < CUATRO) or (nota_segundo_parcial < CUATRO) 

if hay_alguna_nota_invalida:
    print("Ha ingresado al menos una nota invalida")
elif promociona:
    print("Alumno promocionado")
elif aprueba:
    print("Alumno aprobado")
else:
    print("El alumno debe recuperar al menos un examen")

### Otra forma de resolverlo

import random

nota_primer_parcial = random.randint(-1,11) # genera un numero al azar en el intervalo [-1,11]
nota_segundo_parcial = random.randint(-1,11)

CERO = 0
CUATRO = 4
SIETE = 7
DIEZ = 10

hay_alguna_nota_invalida = not (CERO <= nota_primer_parcial <= DIEZ and CERO <= nota_segundo_parcial <= DIEZ)   
promociona = (nota_primer_parcial >= SIETE) and (nota_segundo_parcial >= SIETE)
aprueba = (nota_primer_parcial >= CUATRO) and (nota_segundo_parcial >= CUATRO)   

if hay_alguna_nota_invalida:
    print(f"Notas: [{nota_primer_parcial},{nota_segundo_parcial}] ==> Ha ingresado al menos una nota invalida")
elif promociona:
    print(f"Notas: [{nota_primer_parcial},{nota_segundo_parcial}] ==> Alumno promocionado")
elif aprueba:
    print(f"Notas: [{nota_primer_parcial},{nota_segundo_parcial}] ==> Alumno aprobado")
else:
    print(f"Notas: [{nota_primer_parcial},{nota_segundo_parcial}] ==> El alumno debe recuperar al menos un examen")


################################ CICLOS ################################

"""
Leer numeros hasta que se ingrese un cero. Mostrar la suma 
"""

numero = float(input("Ingrese un numero: "))
suma = 0
while numero != 0:
    suma += numero
    numero = float(input("Ingrese un numero: "))

print(f"La suma es igual a {suma}")


###### Version con generacion de numeros al azar

"""
Leer numeros hasta que se ingrese un cero. Mostrar la suma 
"""

import random

numero = random.randint(0,10000)
print(f"El numero actual es {numero}")
contador = 1
suma = 0
while numero != 0:
    suma += numero
    numero = random.randint(0,10000)
    contador+= 1
    print(f"El numero actual es {numero}")

print(f"La suma es igual a {suma}\nLa cantidad de numeros generados hasta que aparecio el 0 es igual a {contador} ")

"""
Leer 10 numeros desde el teclado. Mostrar la suma
"""

suma = 0
for i in range(10):
    numero = int(input("Ingrese un numero: "))
    suma += numero 

print(f"La suma es igual a {suma}")

"""
Ejercicio 040

Escribir un programa que permita ingresar dos numeros enteros a y b
El programa debe mostrar:
La suma de los numeros 
La suma de los suma de los numeros pares entre a y b
El producto de los numeros impares entre a y b
"""

a = int(input("Ingrese el primer numero: "))
b = int(input("Ahora, ingrese el segundo numero: "))

suma = 0
suma_pares = 0
producto_impares = 1

for i in range(a, b+1):
    suma += i
    if i % 2 == 0:
        suma_pares += i
    else:
        producto_impares *= i

print(f"La suma entre {a} y {b} es igual a {suma}\nLa suma de los numeros pares entre {a} y {b} es igual a {suma_pares}\nLa suma de los numeros impares entre {a} y {b} es igual a {producto_impares}")

n = float('inf')  # declaracion de la variable n que tiende a infinito

