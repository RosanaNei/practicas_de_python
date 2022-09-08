""" def creador_dict( de):
    '''Recibe una  de de caracteres y regresa un diccionario con las palabras (keys) y conteo (value)'''
    lista_1=  de.split()
    dict_1={}
    for i in lista_1:
        if i in dict_1:
            dict_1[i] +=1
        else:
            dict_1[i]= 1
    return dict_1

def contador_dict(dictionario):
    '''Recibe un diccionario y regresa una tupla: la palabra mas repetida y cuantas veces aparece'''
    palabra_frecuente= ''
    cantidad=0
    for keys,values in dictionario.items():
        if values > cantidad:
            cantidad= values
            palabra_frecuente= keys
    return palabra_frecuente,cantidad

entrada='Ingrese su  de de caracteres cadena '
print(creador_dict(entrada))
print(contador_dict(creador_dict(entrada)))
 """

def maximo_comun_divisor(x, y):
    
    if x < y:
        maximo_comun_divisor(y, x) 
    while y != 0:
        x, y = y, x % y
    return x

print(maximo_comun_divisor(436, 400))

#este es una cagada, porque tiene que buscar en todo el rango de b
def mcd(a,b):
    mcd = 1
    for k in range(b,0,-1):
        if a % k == 0 and b % k == 0:
            mcd = k
            break
    return mcd

print(mcd(400, 436))

def maximo_comun_divisor_recursivo(a, b):
    if b == 0:
        return a
    return maximo_comun_divisor_recursivo(b, a % b)

print(maximo_comun_divisor_recursivo(400, 436))

def min_comun_multiplo(a, b):
    mcm = (a*b / maximo_comun_divisor(a, b) )
    return mcm
print(int(min_comun_multiplo (20, 6)))

