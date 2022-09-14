#LA VARIABLE GLOBAL ES ACCESIBLE AL AMBITO DE LA FUNCION (QUE ES LOCAL)
x = 'esglobal'
def foo():
    print(f'acá está x: {x} ')

foo()
print(f'acá está de nuevo: {x} ')

 # SI INTENTO CAMBIAR EL VALOR DE X DENTRO DE LA FC, ME VA A DAR ERROR XQ NO ESTÁ DECLARADA
#UnboundLocalError: local variable 'x' referenced before assignment -- #Error local no vinculado: variable local 'x' referenciada antes de la asignación
"""
x = 'esglobal'
def foo():
    x = x*2
    print(x)

foo()
print(f'acá está de nuevo: {x} ') """

#si INTENTO ACCEDER A UNA VARIABLE LOCAL DESDE EL AMBITO GLOBAL, TAMBIEN DA ERROR

""" def foo():
    y = "local"

foo()
print(y) #NameError: name 'y' is not defined """

#CASTEANDO LAS VARIABLES
x = "global "

def foo():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)

foo()
print(x) #la variable global cambio al valor que se le asigno dentro de la fc 

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

x = 'esglobal'
def foo():
    print(f'acá está x dentro de la fc: {x} ')

foo()
print(f'acá está de nuevo: {x} ')

def prueba_ambitos():
    def hacer_local():
        algo = "algo local"
    def hacer_nonlocal():
        nonlocal algo
        algo = "algo no local"
    def hacer_global():
        global algo
        algo = "algo global"
    algo = "algo de prueba"
    hacer_local()
    print("Luego de la asignación local:", algo)
    hacer_nonlocal()
    print("Luego de la asignación no local:", algo)
    hacer_global()
    print("Luego de la asignación global:", algo)

prueba_ambitos()
print("In global scope:", algo)

