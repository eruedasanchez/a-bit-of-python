import random

FEBRERO = 2
ABRIL = 4
JUNIO = 6
SEPTIEMBRE = 9
NOVIEMBRE = 11

def isbisiesto(anio):
    return anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0  

def obtener_cantidad_dias_del_mes(mes,anio):
    cantidad = 31
    if mes in (ABRIL, JUNIO, SEPTIEMBRE, NOVIEMBRE):
        cantidad = 30
    elif mes == FEBRERO:
        cantidad = 28
        if isbisiesto(anio):
            cantidad = 29   
    
    return cantidad

def obtener_fecha_random(anio):
    mes = random.randint(1,12)
    dia = random.randint(1,obtener_cantidad_dias_del_mes(mes,anio))

    return (anio*10000) + (mes*100) + dia  # = aaaammdd

def calcular_anio(aaaammdd):
    """
    Retorna el año de una fecha
    
    fecha//10000 #AAAA <== |MMDD
    """
    return aaaammdd//10000

def calcular_mes(aaaammdd):
    """
    Retorna el mes de una fecha
    
    AAAA| ==> MM <== | DD   ---> (fecha//100) == AAAAMM y (fecha//100)%100 == MM
    """
    anio_mes = aaaammdd//100
    mes = anio_mes % 100
    return mes

def calcular_dia(aaaammdd):
    """
    Retorna el dia de una fecha
    
    fecha%100 #AAAAMM| ==> DD
    """
    return aaaammdd%100

def str_fecha(aaaammdd):
    anio = calcular_anio(aaaammdd)         # fecha//10000 #AAAA <== |MMDD             
    dia = calcular_dia(aaaammdd)           # fecha%100 #AAAAMM| ==> DD             
    mes = calcular_mes(aaaammdd)           # AAAA| ==> MM <== | DD   ---> (fecha//100) == AAAAMM y (fecha//100)%100 == MM    
    return f"{dia:02}/{mes:02}/{anio:04}"  #:02 incorcopa 2 digitos a la variable

"""
PROGRAMA PRINCIPAL
"""
def main():
    fecha = int(20230601)            #AAAAMMDD
    print(str_fecha(fecha))
    f = obtener_fecha_random(2023)
    print(str_fecha(f))


main() # LLAMO A LA FUNCION PRINCIPAL

