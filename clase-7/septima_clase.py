"""
Ejercicio 033

La farmacia sindical efectua descuentos a sus afiliados segun el
importe de la compra con la siguiente escala:

Menor de 5500.0 el descuento es del 4.5%
Entre 5500.0 y 10000.0 el descuento es del 8%
Mas de 10000.0 el descuento es del 10.5%

Escribir un programa que reciba un importe e informe:
el descuento y el precio neto a cobrar, con mensajes aleatorios.
"""

CINCO_MIL_QUINIENTOS = 5500.0
DIEZ_MIL = 10000.0

CUATRO_PUNTO_CINCO_PORCIENTO = 0.045
OCHO_PORCIENTO = 0.08
DIEZ_PUNTO_CINCO_PORCIENTO = 0.105

importe = float(input("Ingrese un importe: "))

if importe > 0:
    if importe < CINCO_MIL_QUINIENTOS:
        descuento = importe * CUATRO_PUNTO_CINCO_PORCIENTO  
    elif importe <= DIEZ_MIL:
        descuento = importe * OCHO_PORCIENTO  
    else:
        descuento = importe * DIEZ_PUNTO_CINCO_PORCIENTO  
    
    precio_neto = importe - descuento
    print(f"Ingreso un importe de ${importe}.\nPor lo tanto, obtiene un descuento de ${descuento} y el precio neto es de ${precio_neto}")
else:
    print("ingrese un valor mayor a cero (0)")

"""
Ejercicio 030

Escribir un programa que permita al usuario ingresar dos numeros enteros.
La computadora debe indicar si el mayor es divisible por el menor.

(Un numero entero a es divisible por un numero entero b cuando 
el resto de la division entre a y b es 0)
"""

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

if a > b:
    if a % b == 0:
        print(f"El numero {a} es divisible por {b}")
    else:
        print(f"El numero {a} no es divisible por {b}")
elif b % a == 0:
        print(f"El numero {b} es divisible por {a}")
else:
        print(f"El numero {b} no es divisible por {a}")


