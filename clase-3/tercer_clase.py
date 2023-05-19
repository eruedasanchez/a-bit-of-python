# Tercer clase del curso de Python

# Ejercicio 2 extraido de la Ejercitacion 1

# Escribir un programa que solicite al usuario su nombre y su edad, y luego muestre por pantalla 
# un mensaje que diga "Hola, [nombre]. Tu edad es [edad] años."

# Ejemplo de ejecución:
# Ingrese su nombre: Juan
# Ingrese su edad: 30
# Hola, Juan. Tu edad es 30 años.

# nombre = input("Ingrese su nombre: ")
# edad = int(input("Ingrese su edad: ")) 
# print("Hola,", nombre, ". Tu edad es", edad, "años")

# Ejercicio 5 extraido de la Ejercitacion 1

"""
Escribir un programa que solicite al usuario ingresar dos notas de un
alumno. El programa debe mostrar por pantalla el promedio de las notas
de la siguiente manera: 
"Notas: [nota1] , [nota2] ==> promedio: [(nota1+nota2)/2]".
Ejemplo: Si el usuario ingresa 7 y 8, el programa debe mostrar por 
pantalla: "Notas: 7 , 8 ==> promedio: 7.5".
"""

# primer_nota = int(input("Bienvenido. Ingrese la primer nota del alumno: ")) 
# segunda_nota = int(input("Ahora, ingrese la segunda nota del alumno: "))
# promedio = (primer_nota + segunda_nota) / 2
# print("Notas:", primer_nota, ",", segunda_nota, "===>", "promedio:", promedio)

# Ejercicio 8 extraido de la Ejercitacion 1

"""
Escribir un programa que permita ingresar el valor monetario de una hora de trabajo y 
la cantidad de horas trabajadas por día, para calcular el salario semanal de un 
trabajador que trabaja todos los días hábiles y la mitad de las horas del día hábil
los sábados, suponiendo que todas las horas tienen el mismo valor."
"""

DIAS_HABILES = 5
valor_hora_trabajo = float(input("Ingrese el valor monetario de una hora de trabajo: "))
jornada_laboral = int(input("Ingrese la cantidad de horas trabajadas por día: "))
salario_diario = valor_hora_trabajo * jornada_laboral
salario_lun_vie = salario_diario * DIAS_HABILES  
salario_sabado = valor_hora_trabajo * (jornada_laboral / 2) 
salario_semanal_total = salario_lun_vie + salario_sabado
print("El salario semanal del empleado es $", salario_semanal_total) 






