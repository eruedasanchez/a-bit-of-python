"""
Ejercicio 023

Escribir un programa que permita ingresar tres numeros enteros y mostrar el mayor, el menor
y el valor que se encuentra en el medio. Por ejemplo, si se ingresan los numeros 5,3 y 7, el
programa debe mostrar el numero 3 como el menor, el numero 7 como el mayor y el numero 5
como el que esta en el medio 
"""

primer_numero = int(input("Ingrese el primer numero: "))
segundo_numero = int(input("Ingrese el segundo numero: "))
tercer_numero = int(input("Ingrese el tercer numero: "))

mayor = int() 
medio = int()
menor = int()

if primer_numero > segundo_numero and primer_numero > tercer_numero:
    mayor = primer_numero
    if segundo_numero > tercer_numero:
        menor = tercer_numero
        medio = segundo_numero
    else:
        menor = segundo_numero 
        medio = tercer_numero

if segundo_numero > primer_numero and segundo_numero > tercer_numero:
    mayor = segundo_numero
    if primer_numero > tercer_numero:
        menor = tercer_numero
        medio = primer_numero
    else:
        menor = primer_numero 
        medio = tercer_numero

if tercer_numero > primer_numero and tercer_numero > segundo_numero:
    mayor = tercer_numero
    if primer_numero > segundo_numero:
        menor = segundo_numero
        medio = primer_numero
    else:
        menor = primer_numero 
        medio = segundo_numero

print(f"El menor numero es {menor}")
print(f"El numero del medio es {medio}")
print(f"El mayor numero es {mayor}")

"""
Ejercicio 027

Escribir un programa que permita ingresar una edad (entre 1 y 120 años), 
un genero ('F' para mujeres, 'M' para hombres) y un nombre.
En caso de haber ingresado valores erroneos (edad fuera de rango o genero invalido),
informar tal situacion indicando el nombre de la persona.
Si los datos estan bien ingresados, el programa debe indicar, sabiendo que las mujeres
se jubilan con 60 años o mas y los hombres con 65 años o mas, si la persona esta en edad
de jubilarse. 
"""

MASCULINO = "M"
FEMENINO = "F"
UNO = 1
CIENTO_VEINTE = 120
SESENTA = 60
SESENTA_CINCO = 65
nombre = input("Ingrese su nombre: ").title()  # .title() primera letra a mayuscula de cada palabra 
edad = int(input("Ingrese su edad: ")) 
genero = input("Ingrese su genero: ").upper()  # .upper() convierte todo el string a mayuscula
edad_en_rango = UNO <= edad <= CIENTO_VEINTE 
genero_valido = genero == MASCULINO or genero == FEMENINO 

if not(edad_en_rango) or not(genero_valido):
    print(f"{nombre} su edad o genero son invalidos")
else:
    # edad y genero validos
    if genero == FEMENINO:
        if edad >= SESENTA: 
            print(f"{nombre} esta en edad de jubilarse")
        else:
            print(f"{nombre} no esta en edad de jubilarse")
    else:
        if edad >= SESENTA_CINCO:
            print(f"{nombre} esta en edad de jubilarse")
        else:
            print(f"{nombre} no esta en edad de jubilarse")


