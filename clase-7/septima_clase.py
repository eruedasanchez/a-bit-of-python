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

# CINCO_MIL_QUINIENTOS = 5500.0
# DIEZ_MIL = 10000.0

# CUATRO_PUNTO_CINCO_PORCIENTO = 0.045
# OCHO_PORCIENTO = 0.08
# DIEZ_PUNTO_CINCO_PORCIENTO = 0.105

# importe = float(input("Ingrese un importe: "))

# if importe > 0:
#     if importe < CINCO_MIL_QUINIENTOS:
#         descuento = importe * CUATRO_PUNTO_CINCO_PORCIENTO  
#     elif importe <= DIEZ_MIL:
#         descuento = importe * OCHO_PORCIENTO  
#     else:
#         descuento = importe * DIEZ_PUNTO_CINCO_PORCIENTO  
    
#     precio_neto = importe - descuento
#     print(f"Ingreso un importe de ${importe}.\nPor lo tanto, obtiene un descuento de ${descuento} y el precio neto es de ${precio_neto}")
# else:
#     print("ingrese un valor mayor a cero (0)")

"""
Ejercicio 030

Escribir un programa que permita al usuario ingresar dos numeros enteros.
La computadora debe indicar si el mayor es divisible por el menor.

(Un numero entero a es divisible por un numero entero b cuando 
el resto de la division entre a y b es 0)
"""

# a = int(input("Ingrese el primer numero: "))
# b = int(input("Ingrese el segundo numero: "))

# if a > b:
#     if a % b == 0:
#         print(f"El numero {a} es divisible por {b}")
#     else:
#         print(f"El numero {a} no es divisible por {b}")
# elif b % a == 0:
#         print(f"El numero {b} es divisible por {a}")
# else:
#         print(f"El numero {b} no es divisible por {a}")

# from random import randint # (otra manera de importar el modulo random y llamar a randint)


"""
Ejercicio 042

Escribir un programa que lea numeros enteros hasta que se ingrese un 0, y muestre el promedio
de los numeros ingresados
"""

# CERO = 0
# numero = int(input("Ingrese un numero entero: "))
# cant_ingresados = 0
# suma_ingresados = 0

# while numero != CERO:
#     cant_ingresados += 1
#     suma_ingresados += numero
#     numero = int(input("Ingrese un numero entero: "))

# if cant_ingresados != CERO:
#     promedio = suma_ingresados / cant_ingresados
# else:
#     promedio = 0

# print(f"Se ingresaron {cant_ingresados} numeros hasta la primera aparicion de un 0.\n La suma de los numeros ingresados es igual a {suma_ingresados}\n Por ultimo, el promedio de los numeros ingresados es igual a {promedio}")

"""
Ejercicio 059

Escribir un programa para un negocio de venta de granos 
que desea controlar las ventas realizadas. De cada venta
ingresa el importe total y un codigo que indica la forma
de pago.

Los codigos pueden ser:
C: cheque, 20% de recargo
E: efectivo, 10% descuento
T: con tarjeta, 12% de recargo

Se debe ingresar una F para finalizar el dia de venta y arrojar los siguientes totales.

**********************************
Forma de Pago      Total
**********************************
Efectivo en Caja   $ xxxx.xx
Tarjeta/Credito    $ xxxx.xx
Cheques            $ xxxx.xx
Total de Venta     $ xxxx.xx
"""

CHEQUE = "C"
EFECTIVO = "E"
TARJETA = "T"
FINALIZADO = "F"
RECARGO_CHEQUE = 0.2
RECARGO_TARJETA = 0.12
DESCUENTO_EFECTIVO = 0.1

estado_actual_dia = input("Ingrese F si termino el dia y desea ver los totales recaudados; o cualquier otra tecla en caso contrario: ")
total_cheque = 0
total_efectivo = 0
total_tarjeta = 0
total_ventas = 0

while estado_actual_dia != FINALIZADO:
    importe = float(input("Ingrese el importe de la venta: "))
    codigo_pago = input("Ingrese el codigo de pago (C(heque), E(fectivo) o T(arjeta)): ")
    if codigo_pago == CHEQUE:
        recargo = importe * RECARGO_CHEQUE 
        importe_final = importe + recargo
        total_cheque += importe_final
    elif codigo_pago == EFECTIVO:
        descuento = importe * DESCUENTO_EFECTIVO 
        importe_final = importe - descuento
        total_efectivo += importe_final
    elif codigo_pago == TARJETA:
        recargo = importe * RECARGO_TARJETA 
        importe_final = importe + recargo
        total_tarjeta += importe_final
    else:
        print("El medio de pago elegido es incorrecto. Por ingrese, C, E o T.")
    
    estado_actual_dia = input("Ingrese F si termino el dia y desea ver los totales recaudados; o cualquier otra tecla en caso contrario: ")

total_ventas = total_cheque + total_efectivo + total_tarjeta
print(f"Total ventas: {total_ventas}, Total Efectivo: {total_efectivo}, Total Cheque: {total_cheque}, Total Tarjeta: {total_tarjeta}")



