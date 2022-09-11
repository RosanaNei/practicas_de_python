#LISTAS
# Creando listas
#Las listas permiten almacenar objetos mediante un orden definido y con posibilidad de 
# duplicados. Las listas son estructuras de datos mutables, lo que significa que podemos 
# añadir, eliminar o modificar sus elementos

empty_list = []
languages = ['Python', 'Ruby', 'Javascript']
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13]
data = ['Tenerife', {'cielo': 'limpio', 'temp': 24}, 3718, (28.2933947, -16.5226597)]
#Nota: Una lista puede contener tipos de datos heterogéneos, lo que la hace una estructura 
# de datos muy versátil.
print(list('Python'))

def mostrar(lista):
    for palabra in lista:
        print (palabra)
    print(f'Esta es la segunda palabra: {lista[1]}')
       
shopping = ['Agua', 'Huevos', 'Aceite']
mostrar(shopping)

#Trocear una lista. El troceado de listas funciona de manera totalmente análoga al troceado 
# de cadenas. Veamos algunos ejemplos:

shopping = ['Agua', 'Huevos', 'Aceite','jamón', 'maníes']
print(shopping[0:3])
print(shopping[:3])
print(shopping[2:4])
print(shopping[-1:-4:-1])
# Equivale a invertir la lista
print(shopping[::-1])

#Invertir una lista
# Conservando la lista original:Mediante troceado de listas con step negativo:
shopping[::-1]
#Conservando la lista original:Mediante la función reversed():
list(reversed(shopping))
#Modificando la lista original: Utilizando la función reverse() (nótese que es sin «d» al final):
shopping.reverse()
#Añadir al final de la lista
shopping.append('Atún')
#CREANDO DESDE VACÍO
#Una forma muy habitual de trabajar con listas es empezar con una vacía e ir añadiendo elementos 
# poco a poco. Se podría hablar de un patrón creación.
numeros_pares = []
for i in range (20):
    if i % 2 ==0:
        numeros_pares.append(i)
        
print(numeros_pares)

#Combinar listas sin modificarlas
selling = ['jabón', 'detergente', 'sopa']
all_together = shopping + selling
print(all_together)
#combinar modificando
shopping.extend(selling)
print(shopping)
#Hay que tener en cuenta que extend() funciona adecuadamente si pasamos una lista como argumento. 
# En otro caso, quizás los resultados no sean los esperados. Veamos un ejemplo:
shopping.extend('limon')
print(shopping)
shopping.append('limon')
print(shopping)

#BORRAR ELEMENTOS. 
# Python nos ofrece, al menos, cuatro formas para borrar elementos en una lista:

# Por su índice:Mediante la función del():
shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
del(shopping[3])
print(shopping)
#Por su valor: Mediante la función remove():
shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
shopping.remove('Huevos')
print(shopping)
#Por su índice (con extracción):
shopping.pop(2)
print(shopping)
#Por su rango: Mediante troceado de listas:
shopping[1:4] = []

#BORRADO COMPLETO DE LA LISTA 
# Utilizando la función clear():
shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
shopping.clear()
#Reinicializando» la lista a vacío con []:
shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
shopping = []

#Encontrar un elemento. Si queremos descubrir el índice que corresponde a un determinado valor dentro la lista podemos 
# usar la función index() para ello:
shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
print(shopping.index('Huevos')) 
#si el elemento que buscamos no está en la lista, obtendremos un error. Y Si buscamos un valor que existe más de una 
# vez en una lista, la función index() sólo nos devolverá el índice de la primera ocurrencia.

#PERTENENCIA DE UN ELEMENTO: Si queremos comprobar la existencia de un determinado elemento en una lista, podríamos 
# buscar su índice con el operador in:  El operador in siempre devuelve un valor booleano, es decir, verdadero o falso. 
shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
'Aceite' in shopping
'Pollo' in shopping

#NUMERO DE OCURRENCIAS Para contar cuántas veces aparece un determinado valor dentro de una lista podemos usar la 
# función count():
sheldon_greeting = ['Penny', 'Penny', 'Penny']
sheldon_greeting.count('Howard')
sheldon_greeting.count('Penny')

#Convertir lista a cadena de texto Dada una lista, podemos convetirla a una cadena de texto, uniendo todos sus 
# elementos mediante algún separador. ATENCION!! join() sólo funciona si todos sus elementos son cadenas de texto
shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
','.join(shopping)
' '.join(shopping)
'|'.join(shopping)

#Ordenar una lista.dos formas de ordenar los elementos de una lista:
# Conservando lista original:Mediante la función sorted() que devuelve una nueva lista ordenada:
shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
sorted(shopping)

#Modificando la lista original:Mediante la función sort():
shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
shopping.sort()
print(f'esta lista está modificada {shopping} ')
#Ambos métodos admiten un parámetro «booleano» 
# reverse para indicar si queremos que la ordenación se haga en sentido inverso:
shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
sorted(shopping, reverse=True)
print(sorted(shopping, reverse=True))
print(shopping)

#BONITA APLICACION DE ESTAS PROPIEDADES - CORRECION DE FECHA
input_date = '12/31/20'

splitted_date = input_date.split('/')
day = splitted_date[1]
month = splitted_date[0]
year = '20' + splitted_date[2]

output_date = '-'.join([day, month, year])
print(output_date)

#ITERAR USANDO ENUMERACIÓN y sin usarla
shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']

for i, product in enumerate(shopping):
    print(i + 1, product)

for product in shopping:
    print(product)

#ITERAR SOBRE MÚLTIPLES LISTAS - iterar sobre múltiples listas en paralelo utilizando la función zip():

shopping = ['Agua', 'Aceite', 'Arroz']
details = ['mineral natural', 'de oliva virgen', 'basmati']

for product, detail in zip(shopping, details):
    print(product, detail)

print (list(zip(shopping, details)))
 #crea una lista con nuevos grupos, con los items integrados

v1 = [4, 3, 8, 1]
v2 = [9, 2, 7, 3]

for va, vb in zip(v1, v2):
    print (va * vb)



