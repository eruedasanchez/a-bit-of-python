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

# PRIMERA = 1
# SEGUNDA = 2
# TERCERA = 3
# ESTA_HAMBRIENTO = 'S'
# CANTIDAD_TANDAS = 3
# total_alimento_recibido = 0
# sigue_con_hambre = True
# tanda = 1

# while 1 <= tanda <= CANTIDAD_TANDAS and sigue_con_hambre:
#     print(f"Tanda de comida {tanda} de {CANTIDAD_TANDAS}")
#     cant_alimento = int(input(f"Ingrese la cantidad de alimento (en kg) que come el animal en la tanda {tanda}: "))
#     if tanda == PRIMERA:
#         cant_primera_tanda = cant_alimento
#         maxima_tanda_cant = PRIMERA
#         maxima_cantidad = cant_primera_tanda  
#     elif tanda == SEGUNDA:
#         cant_segunda_tanda = cant_alimento
#         if cant_segunda_tanda > maxima_cantidad:
#             maxima_tanda_cant = SEGUNDA
#             maxima_cantidad = cant_segunda_tanda
#     else:
#         cant_tercera_tanda = cant_alimento
#         if cant_tercera_tanda > maxima_cantidad:
#             maxima_tanda_cant = TERCERA
#             maxima_cantidad = cant_tercera_tanda
        
#     total_alimento_recibido += cant_alimento
#     if tanda != CANTIDAD_TANDAS: 
#         sigue_con_hambre = input("Continua comiendo [S/N]: ").upper() == ESTA_HAMBRIENTO
#     else:
#         sigue_con_hambre = False
#     tanda += 1

# print(f"El animal recibio mas comida en la tanda {maxima_tanda_cant} y fue de {maxima_cantidad} kg")
# print(f"El total de alimento recibido por el animal fue de {total_alimento_recibido} kg")
# print(f"El promedio de alimento por tanda fue de {total_alimento_recibido / (tanda-1)}")

"""
Ejercicio 066b

La biblioteca de la ciudad necesita organizar y hacer un recuento de los libros 
que tiene en sus estantes. Para cada uno de los estantes (usando 'F' para indicar 
el fin de los estantes), se deben ingresar 15 libros, y para cada libro, se debe ingresar su nombre,
género (usando 'I' para Infantil, 'N' para Novela, o 'H' para Historia), 
y cantidad de páginas (mayor a 0). Una vez que se han ingresado los datos de 1 estante, 
se debe mostrar por pantalla el nombre del libro con la mayor cantidad de páginas y
su cantidad correspondiente. Al finalizar el ingreso de datos de todos los estantes, 
se deben mostrar la cantidad de libros por género.
"""

# FINALIZAR_CARGA = 'F'
# INFANTIL = 'I'
# NOVELA = 'N'
# HISTORIA = 'H'
# CANT_LIBROS_ESTANTE = 15

# finalizar_carga_estantes = False
# numero_estante = 1
# total_infantil = 0
# total_novela = 0
# total_historia = 0

# while not finalizar_carga_estantes:
#     max_paginas = 0
#     print(f"Vamos a cargar {CANT_LIBROS_ESTANTE} libros al estante numero {numero_estante}")
#     for libro in range(CANT_LIBROS_ESTANTE):
#         nombre = input(f"Ingrese el nombre del libro {libro+1}: ")
#         paginas_libro_actual = int(input(f"Ingrese la cantidad de páginas del libro {libro+1}: "))

#         if paginas_libro_actual > max_paginas:
#             nombre_max_paginas = nombre
#             max_paginas = paginas_libro_actual
        
#         genero = input(f"Ingrese el genero del libro {libro+1} ('I' para Infantil, 'N' para Novela o 'H' para Historia): ")
#         while genero not in (INFANTIL, NOVELA, HISTORIA):
#             print("Error en el genero.")
#             genero = input(f"Ingrese el genero del libro {libro+1} ('I' para Infantil, 'N' para Novela o 'H' para Historia): ")
        
#         if genero == INFANTIL:
#             total_infantil += 1
#         elif genero == NOVELA:
#             total_novela += 1
#         else:
#             total_historia += 1
    
#     print(f"El nombre del libro con la mayor cantidad de páginas del estante {numero_estante} es {nombre_max_paginas} y su cantidad es de {max_paginas}")
#     finalizar_carga_estantes = input("Presione 'F' si finalizo de cargar todos los estantes o cualquier otra tecla en caso contrario: ").upper() == FINALIZAR_CARGA
#     numero_estante += 1

# print(f"La cantidad de libros de genero infantil son {total_infantil}.")    
# print(f"La cantidad de libros de genero novela son {total_novela}.")
# print(f"La cantidad de libros de genero de historia son {total_historia}.")

"""
Ejercicio adicional

Contar la cantidad de palabras del siguiente texto:

La biblioteca de la ciudad necesita organizar y hacer un recuento de los libros 
que tiene en sus estantes. Para cada uno de los estantes (usando 'F' para indicar 
el fin de los estantes), se deben ingresar 15 libros, y para cada libro, se debe ingresar su nombre,
género (usando 'I' para Infantil, 'N' para Novela, o 'H' para Historia), 
y cantidad de páginas (mayor a 0). Una vez que se han ingresado los datos de 1 estante, 
se debe mostrar por pantalla el nombre del libro con la mayor cantidad de páginas y
su cantidad correspondiente. Al finalizar el ingreso de datos de todos los estantes, 
se deben mostrar la cantidad de libros por género.
"""

texto = """La biblioteca  de   la ciudad necesita organizar y hacer un recuento de los libros hola pepe juancito"""

ESPACIO = ' '
cant_palabras = 0
i = 0

while i < len(texto):
    palabra = ""
    while i < len(texto) and texto[i] != ESPACIO:
        palabra += texto[i]
        i += 1
    
    if len(palabra) > 0:
        cant_palabras += 1
    else:
        i += 1

print(f"La cantidad de palabras que tiene el texto son {cant_palabras}")



