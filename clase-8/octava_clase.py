"""
Ejercicio 064

Un animal en rehabilitacion despues de una cirugia requiere ser alimentado y
monitoreado en un zoologico. Se alimenta al animal 3 veces al dia y se le da
de comer hasta que ya no tenga ganas de comer.
Por cada tanda de comida, se debe ingresar la cantidad de alimento en kg (numero entero)
que se le dio y se le debe preguntar al animal si quiere seguir comiendo ('S', 'N').
Se desea conocer:
- Cual de las 3 comidas fue la que el animal comio mas cantidad de alimento y cuanto fue esa cantidad 
- El total en kg de alimento recibido
- Promedio de alimento por tanda
"""

PRIMERA = 1
SEGUNDA = 2
TERCERA = 3
ESTA_HAMBRIENTO = 'S'
CANTIDAD_TANDAS = 3
total_alimento_recibido = 0
sigue_con_hambre = True
tanda = 1

while 1 <= tanda <= CANTIDAD_TANDAS and sigue_con_hambre:
    print(f"Tanda de comida {tanda} de {CANTIDAD_TANDAS}")
    cant_alimento = int(input(f"Ingrese la cantidad de alimento (en kg) que come el animal en la tanda {tanda}: "))
    if tanda == PRIMERA:
        cant_primera_tanda = cant_alimento
        maxima_tanda_cant = PRIMERA
        maxima_cantidad = cant_primera_tanda  
    elif tanda == SEGUNDA:
        cant_segunda_tanda = cant_alimento
        if cant_segunda_tanda > maxima_cantidad:
            maxima_tanda_cant = SEGUNDA
            maxima_cantidad = cant_segunda_tanda
    else:
        cant_tercera_tanda = cant_alimento
        if cant_tercera_tanda > maxima_cantidad:
            maxima_tanda_cant = TERCERA
            maxima_cantidad = cant_tercera_tanda
        
    total_alimento_recibido += cant_alimento
    if tanda != CANTIDAD_TANDAS: 
        sigue_con_hambre = input("Continua comiendo [S/N]: ").upper() == ESTA_HAMBRIENTO
    else:
        sigue_con_hambre = False
    tanda += 1

print(f"El animal recibio mas comida en la tanda {maxima_tanda_cant} y fue de {maxima_cantidad} kg")
print(f"El total de alimento recibido por el animal fue de {total_alimento_recibido} kg")
print(f"El promedio de alimento por tanda fue de {total_alimento_recibido / (tanda-1)}")






