""" 
def superficie_cuadrado(plado):
    return plado**2

lado = float(input('ingrese'))
print(f'la superficie del cuadrado de lado {lado} es {superficie_cuadrado(lado)}')
print(superficie_cuadrado)
help(superficie_cuadrado)

def suma(num1, num2, num3=6):
    # el parametro por defecto siempre va al final
    return num1 + num2 + num3
    
#pasando un diccionario     
print(f'el valor es {suma(4, 19,23)}')
print(f'el valor es {suma(6,7)}') #l falta del un parametro no importa xq hay uno por defecto 

def saludo_ingles(a):
    print(f'hi, {a}')

def saludo_espagnol(a):
    print(f'hola, {a}')
    
a= input('ingrese el nombre ')
saludadores = {'en': saludo_ingles(a), 'es':saludo_espagnol(a)}
print(saludadores)

#*args - pasar un numero inderterminado de argumentos
def suma_cambiante(*args):
    result=0
    for x in args:
        result += x
    return result

print(suma_cambiante(2, 2, 2, 2, 2))
print(f'el resultado es {suma_cambiante(5, 7, 8, 6, 5)} ')

#**kwarg para pasar un diccionario
def concatenar(**kwargs):
    
    print(kwargs.values())
    print(kwargs.keys())
    print(kwargs.items())
    
    result=''
    for arg in kwargs.values():
        result += arg
    return result
        
print(concatenar(a = 'codo ', b = 'a ', c = 'codo', d = '!'))


def saludi():
    a = ''
    for i in range(3):
        a = input('ingrese nombre ')
        print (f'hola {a} ')

saludi()

diccionario = {'una': 1, 'dosa': 2, 'tresa': 3}
for clave, valor in diccionario.items():
    print(clave + valor)
    
#SCOPE DE LAS VARIABLES Y SU CASTEO
x = 4
def funcion():
    x = 16
    print(f'la var enclosed es x = {x}')
    def funcion_interna():
        x = 45
        print(f'la local es x = {x}')
    print(funcion_interna())
    
print(f'la global es {x} ')   
funcion()

#acá va la mala práctica     
x = 8
def funcion():
    x = 32
    def funcion_interna():
        nonlocal x
        x = 90
        print(f'la local es x = {x}')
    print(funcion_interna())
    return x
    
print(f'la global es {x} ')   
print(f'la enclosure es {funcion()} ') 

def myfunc1():
  x = 10
  def myfunc2():
    nonlocal x
    x = 20
  myfunc2()
  return x

print(myfunc1())   """

#tres formas de imprimir una lista
def lista_comidas(food):
    for x in food:
        me_comi = 'comí una %s' % x
        me_comi = 'comí una {food}'.format(food=x)
        me_comi = f'comí una {x} '
        print(me_comi)
        
comidas = ['pera', 'manzana', 'banana']
lista_comidas(comidas)