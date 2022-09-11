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
#Borrar elementos. Python nos ofrece, al menos, cuatro formas para borrar elementos en una lista:
# Por su índice:Mediante la función del():
shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
del(shopping[3])
print(shopping)
#Por su valor: Mediante la función remove():
shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
shopping.remove('Huevos')
print(shopping)



