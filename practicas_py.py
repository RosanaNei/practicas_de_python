def superficie_cuadrado(plado):
    '''
    calcula superficie
    '''
    return plado**2

lado = float(input('ingrese'))
print(f'la superficie del cuadrado de lado {lado} es {superficie_cuadrado(lado)}')
print(superficie_cuadrado)
help(superficie_cuadrado)

def suma(num1, num2, num3=6):
    '''
    uso de parametros por defecto, siempre van al final
    '''
    suma = num1 + num2 + num3
    return suma
suma(4, 19,23)
print(f'el valor es {suma(4, 19,23)}')
print(f'el valor es {suma(6,7)}')
    
