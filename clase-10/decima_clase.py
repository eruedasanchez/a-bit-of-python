def calcular_anio(f):
    return f//10000

def calcular_mes(f):
    anio_mes = f//100
    mes = anio_mes % 100
    return mes

def calcular_dia(f):
    return f%100

def str_fecha(f):
    anio = calcular_anio(f)         # fecha//10000 #AAAA <== |MMDD             
    dia = calcular_dia(f)           # fecha%100 #AAAAMM| ==> DD             
    mes = calcular_mes(f)           # AAAA| ==> MM <== | DD   ---> (fecha//100) == AAAAMM y (fecha//100)%100 == MM    
    return f"{dia}/{mes}/{anio}"

"""
PROGRAMA PRINCIPAL
"""
def main():
    fecha = int(19851217)            #AAAAMMDD
    print(str_fecha(fecha))


main() # LLAMO A LA FUNCION PRINCIPAL

