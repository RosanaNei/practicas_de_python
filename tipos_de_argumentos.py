#ARGUMENTOS POSICIONALES son aquellos argumentos que se copian en sus correspondientes parámetros en orden.
#lo que sucede es un mapeo directo entre argumentos y parámetros en el mismo orden que estaban definidos:
def build_cpu(vendor, num_cores, freq):
    return dict(
        vendor=vendor,
        num_cores=num_cores,
        freq=freq
    )
print(build_cpu('AMD', 8, 2.4))
#ARGUMENTOS NOMINALES En esta aproximación los argumentos no son copiados en un orden específico sino que se asignan 
# por nombre a cada parámetro. Ello nos permite salvar el problema de conocer cuál es el orden de los parámetros en la 
# definición de la función. Para utilizarlo, basta con realizar una asignación de cada argumento en la propia llamada a 
# la función. 
def build_cpu(vendor, num_cores, freq):
    return dict(
        vendor=vendor,
        num_cores=num_cores,
        freq=freq
    )

print(build_cpu(vendor='AMD', num_cores=8, freq=2.7))
print(build_cpu(num_cores=8, freq=2.7, vendor='AMD'))
print(build_cpu('INTEL', num_cores=4, freq=3.1))  # Python permite mezclar argumentos posicionales y nominales en la llamada a una función:
#hay que tener en cuenta que, en este escenario, los argumentos posicionales siempre deben ir antes que los  argumentos nominales. Esto tiene 
# mucho sentido ya que, de hacerlo así, Python no tendría forma de discernir a qué parámetro 
# corresponde cada argumento:
""" build_cpu(num_cores=4, 'INTEL', freq=3.1) """ #tira sintax error

#PARAMETROS POR DEFECTO. Es posible especificar valores por defecto en los parámetros de una función. En el caso de que no se proporcione un valor 
# al argumento en la llamada a la función, el parámetro correspondiente tomará el valor definido por defecto.
def build_cpu(vendor, num_cores, freq=2.0):
    return dict(
        vendor=vendor,
        num_cores=num_cores,
        freq=freq
    )
print(build_cpu('INTEL', 2))
print(build_cpu('INTEL', 2, 3.4))  #acá el valor asignado pisa al valor puesto por defecto. Los valores por defecto se declaran cuando se 
#declara la función, no cuando se invoca
def buggy(arg, result=[]):
    result.append(arg)
    print(result)
buggy('a', [])
buggy('b', [])
buggy('a', ['x', 'y', 'z'])
buggy('b', ['x', 'y', 'z'])
buggy('a') #curiosamente, al no pasarle argumentos a result, la a se guarda en la memoria y el siguiente resultado es result = [a, b]
buggy('b') #esto se debe a que es una lista, y las listas son mutables. De ahí la utilidad de las tuplas

#A riesgo de perder el parámetro por defecto, una posible solución sería la siguiente:
def works(arg):
    result = []
    result.append(arg)
    print( result)
works('a')
works('b')
#La forma de arreglar el código anterior utilizando un parámetro con valor por defecto sería utilizar un tipo de dato inmutable y tener 
# en cuenta cuál es la primera llamada:
def nonbuggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)
nonbuggy('a')
nonbuggy('b')
nonbuggy('a', ['x', 'y', 'z'])
nonbuggy('b', ['x', 'y', 'z'])
#Empaquetar/Desempaquetar argumentos
#Empaquetar y descomprimir argumentos en Python. Usamos dos operadores *(para tuplas) y **(para diccionarios)
#EMPAQUETAR/DESEMPAQUETAR ARGUMENTOS POSICIONALES
#Si utilizamos el operador * delante del nombre de un parámetro posicional, estaremos indicando que los argumentos pasados a la función 
# se empaqueten en una tupla:
def test_args(*args):
    print(f'{args=}')
test_args()
test_args(1, 2, 3, 'pescado', 'salado', 'es')

#si queremos pasar una lista como argumento no funciona, xq espera 4 y sólo recibe 1
""" def fun(a, b, c, d):
    print(a, b, c, d) 
my_list = [1, 2, 3, 4]
fun(my_list) """ #Exception has occurred: TypeError fun() missing 3 required positional arguments: 'b', 'c', and 'd'
#DESEMPAQUETANDO Podemos usar * para descomprimir la lista de modo que todos sus elementos 
# puedan pasarse como parámetros diferentes.el no. de argumentos debe ser la misma que la longitud de la lista que 
# estamos desempaquetando para los argumentos.
def fun(a, b, c, d):
    print(a, b, c, d)
my_list = [1, 2, 3, 4]
fun(*my_list)
#La función anterior mySum() "empaqueta" para empaquetar todos los argumentos que recibe esta llamada al método en 
# una sola variable y por eso LOS SUMA!!
def mySum(*args):
    args[0]
    return sum(args) 

print(mySum(1, 2, 3, 4, 5))
print(mySum(10, 20))

def sum_all(v1, v2, *args):
    total = 0
    for value in (v1, v2) + args:
        total += value
    return total

#sum_all() Exception has occurred: TypeErrormissing 2 required positional arguments: 'v1' and 'v2'
sum_all(1, 2)
sum_all(5, 9, 3, 8, 11, 21)
