# Cuarta clase del curso de Python

# print por consola con separadores 

a = 0
b = 1
c = 'pepe'

print(a,b,c,sep='')     # elimina todos los espacios de separacion
print(a,b,c,sep='-')    # coloca un - como elemento de separacion entre los elementos
print(a,b,c,sep='\n')   # salto de linea entre cada elemento


# obtener la impresion 01 pepe
print(a,b,sep='',end=' ')
print(c)

"""
Ejercicio 009 de la ejercitacion 

Escribir un programa que permita ingresar valores del mismo tipo para
las variables num1 y num2. Una vez cargadas, mostrar ambas variables
por pantalla, intercambiar sus valores (que lo cargado en num1 
quede en num2, y viceversa) y volver a mostrarlas actualizadas.
"""

num1 = int(input("Ingrese el valor para la primer variable: "))
num2 = int(input("Ingrese el valor para la segunda variable: "))
print("Ahora vamos a intercambiar sus valores")
tmp = num1
num1 = num2
num2 = tmp
print("Entonces, el valor de la primer variable es", num1,end=' ')
print("y el valor de la segunda variable es", num2)

num1,num2 = num2,num1 # solo en Python (funciona gracias a las estructuras de datos de python... mas adelante)
print(num1,num2)

"""
Ejercicio 016

Escribir un programa que permita al usuario ingresar un periodo de tiempo en segundos.
Luego, el programa debe convertir ese periodo de tiempo a una forma mas legible y comprensible
para el usuario expresando el resultado en dias, horas, minutos y segundos.
El resultado se mostrara en pantalla en un mensaje que indique la cantidad de segundos ingresados y su
equivalente en dias, horas, minutos y segundos.
Ejemplo: 200000 segundos equivalen a 2 dias, 7 horas, 33 minutos y 20 segundos
"""

segundos_ingresados = int(input("Ingrese la cantidad de segundos: "))
SEGUNDOS_POR_DIA = 86400
SEGUNDOS_POR_HORA = 3600
SEGUNDOS_POR_MINUTO = 60

dias = int(segundos_ingresados / SEGUNDOS_POR_DIA)                     # se puede utilizar el operador // que realiza division entera 
segundos_restantes_hora = segundos_ingresados % SEGUNDOS_POR_DIA 

horas = int(segundos_restantes_hora / SEGUNDOS_POR_HORA)   
segundos_restantes_minutos = segundos_restantes_hora % SEGUNDOS_POR_HORA 

minutos = int(segundos_restantes_minutos / SEGUNDOS_POR_MINUTO)   
segundos = segundos_restantes_minutos % SEGUNDOS_POR_MINUTO

print(f"{segundos_ingresados} segundos equivalen a {dias:02} dias, {horas:02} horas, {minutos:02} minutos y {segundos:02} segundos") # f para darle formato al string, :02 expresa el resultado en dos (2) digitos



#27200 segundos

# 1 minuto         -> 60 segundos
# 1hora            -> 3600 segundos
# 1 dia = 24 horas -> 86400 segundos   

"""#
Ejercicio 021

Escribir un programa que permita al usuario ingresar dos numeros enteros
e indicar si el primero es mayor, menor o igual al segundo
"""

primer_numero = int(input("Ingrese el primer numero: "))
segundo_numero = int(input("Ingrese el segundo numero: "))

resultado = f"{primer_numero} y {segundo_numero} son iguales"
if primer_numero > segundo_numero:
    resultado = f"El numero {primer_numero} es mayor a {segundo_numero}"
elif primer_numero < segundo_numero:
    resultado = f"El numero {primer_numero} es menor a {segundo_numero}"

print(resultado)

"""
Ejercicio 022

Escribir un programa que permita al usuario ingresar tres (3) numeros enteros
e indicar cual es el mayor
"""

primer_numero = int(input("Ingrese el primer numero: "))
segundo_numero = int(input("Ingrese el segundo numero: "))
tercer_numero = int(input("Ingrese el tercer numero: "))

resultado = f"{primer_numero}, {segundo_numero} y {tercer_numero} son iguales"
if (primer_numero > segundo_numero) and (primer_numero > tercer_numero) :
    resultado = f"El numero {primer_numero} es mayor a {segundo_numero} y a {tercer_numero}"
else:
    if (segundo_numero > primer_numero) and (segundo_numero > tercer_numero) :
        resultado = f"El numero {segundo_numero} es mayor a {primer_numero} y a {tercer_numero}"
    else:
        if (tercer_numero > primer_numero) and (tercer_numero > segundo_numero) :
            resultado = f"El numero {tercer_numero} es mayor a {primer_numero} y a {segundo_numero}"
            
print(resultado)

# otra manera de resolverlo sin operadores logicos

primer_numero = int(input("Ingrese el primer numero: "))
segundo_numero = int(input("Ingrese el segundo numero: "))
tercer_numero = int(input("Ingrese el tercer numero: "))

mayor = primer_numero

if segundo_numero > mayor:
    mayor = segundo_numero

if tercer_numero > mayor:
    mayor = tercer_numero

resultado = f"El numero maximo entre {primer_numero}, {segundo_numero} y {tercer_numero} es {mayor}"

print(resultado)

"""
Ejercicio 024

Para acceder a cierta atraccion, es necesario cumplir con dos requisitos:
tener al menos 10 años de edad y medir mas de 1,60 metros
(Ojo, tener en cuenta las palabras: mas , al menos y sobre todo la letra y)

Escribir un programa en Python que solicite al usuario su edad y altura
que determine si cumple con los requisitos para subir a la atraccion
Si cumple con ambos requisitos, el programa debe imprimir "¡Puede acceder!" en la pantalla
Si no cumple con algun requisito, el programa debe imprimri un mensaje que indique el motivo por el cual no puede subir  
"""

EDAD_MINIMA_INGRESO = 10
ESTATURA_MINIMA_INGRESO = 1.60
edad = int(input("Ingrese su edad: ")) 
estatura = float(input("Ingrese su estatura en metros: "))

if (edad >= EDAD_MINIMA_INGRESO) and (estatura > ESTATURA_MINIMA_INGRESO):
    print("¡Puede acceder!")
else:
    if not(edad >= 10):
        print("Lo siento, eres demasiado joven para acceder.")
    
    if not(estatura > ESTATURA_MINIMA_INGRESO):
            print("Lo siento, eres demasiado bajo para acceder.")

"""
Ejercicio 025

Para acceder a cierta atraccion, es necesario cumplir con dos requisitos:
ser mayor de 6 años de edad o medir mas de 1,50 metros
(Ojo, tener en cuenta las palabras: mas y sobre todo la letra o)

Escribir un programa en Python que solicite al usuario su edad y altura
que determine si cumple con los requisitos para subir a la atraccion
Si cumple con al menos algun requisito, el programa debe imprimir "¡Puede acceder!" en la pantalla
Si no cumple, el programa debe imprimir un mensaje que indique el motivo por el cual no puede subir  
"""            

EDAD_MINIMA_INGRESO = 7
ESTATURA_MINIMA_INGRESO = 1.50
edad = int(input("Ingrese su edad: ")) 
estatura = float(input("Ingrese su estatura en metros: "))

if (edad >= EDAD_MINIMA_INGRESO) or (estatura > ESTATURA_MINIMA_INGRESO):
    print("¡Puede acceder!")
else:
    print("Lo siento, eres demasiado joven para acceder.")
    print("Lo siento, eres demasiado bajo para acceder.")





