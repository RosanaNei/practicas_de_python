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

print(myfunc1())  

#tres formas de imprimir una lista ' PARA NO ARRIESGAR A CAMBIOS INDESEADOS, SE SUELEN PASAR TUPLAS Y NO LISTAS
def lista_comidas(food):
    food[1] = 'guinda'
    copy_food = food.copy()
    copy_food[2] = 'kiwi'
    copy_food.sort() #ordena alfabéticamente PUEDO USAR CUALQUIER METODO DEL MANEJO DE LISTAS!!!
    for x in copy_food:
        me_comi = 'comí una %s' % x
        me_comi = 'comí una {food}'.format(food=x)
        me_comi = f'comí una {x} '#esta aparece con la version 3.6 de python y es la más copada
        print(me_comi)
        
comidas = ['pera', 'manzana', 'banana', 'carozo']
lista_comidas(comidas)


#FUNCIONES RECURSIVAS
def jugar(intento=1): 
    respuesta = input("¿De qué color es una naranja? ") 
    if respuesta != "naranja": 
        if intento < 3: 
            print ("\nFallaste! Inténtalo de nuevo" )
            intento += 1 
            jugar(intento) # Llamada recursiva 
        else: 
            print( "\nPerdiste!" )
    else:
        print ("\nGanaste!" )
jugar()

for i in range(5):
    if i !=3:
        print(i)
        
i = 1       
while i !=5:   
    i += 1
    print(i) """

def one():
    return 1
#integrando una fucion en un control booleano
if one() == 1:
    print('It works!')
else:
    print('Something is broken')
    
#Si una función no incluye un return de forma explícita, devolverá None de forma implícita:
def empty():
    x = 18

print(empty())

def truthiness(obj):
    if obj:
        print(f'{obj} is True')
    else:
        print(f'{obj} is False')
x = ''
truthiness(x)
#TODAS ESTAS OPCIONES SON False
truthiness(False)

truthiness(None)

truthiness(0)

truthiness(0.0)

truthiness('')

truthiness([])

truthiness(())

truthiness({})

truthiness(set())    
#el resto es evaluado a True- Ejemplos
truthiness(True)

truthiness(1e-10)

truthiness([0])

truthiness(('',))

truthiness(' ')

truthiness('🦆')
#Raíces cuadradas y cúbicas
def sqrt(value):
    return value ** (1/2)
print(sqrt(4))
def cubic(value):
    return value ** (1/3)
print(cubic(27))

print(type('🦆'))

def mi_bella_fc(valor_a, valor_b, valor_c):
    pass            #---la palabra reservada pass permite no hacer nada, y convierte a la funcion en una especie de placeholder
mi_bella_fc('hola', {1, 2, 3}, (5+8))

def suma_cuadrados(x, y):
    return x**2 + y**2
print(suma_cuadrados(2,5))

