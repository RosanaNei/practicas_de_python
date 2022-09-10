#dos iteraciones quen hacen lo mismo, con y sin funcion continue

""" num = 10
while num >= 1:
    num -= 1
    if num % 3 == 0:
        continue
    print(num,end=	',' )

num = 10
while num >= 1:
    num -= 1
    if num % 3 != 0:
       print(num,end= ',')
       
#OPERADOR MORSA := - comparación entre dos métdos
radius = 4.25
perimeter = 2 * 3.14 * radius
if perimeter < 100:
    print('Increase radius to reach minimum perimeter')
print(	f'Actual perimeter: {perimeter}') 

radius = 4.25
if (perimeter := 2 * 3.14 * radius) < 100:
    print('Increase radius to reach minimum perimeter')
print(	f'Actual perimeter: {perimeter}') 

word = 	'Pythom'	
for letter in word:
    print(letter)

palabra = 'Supercalifragilisticoespialidoso'
cont = 0
for letra in palabra:
    if letra in 'aeiou':
        cont +=1
        
print(f'la cant es {cont}')
 

#buscando primis
def es_primo(num, n=2):
    if n >= num//2:
        print("Es primo")
        return True
    elif num % n != 0:
        return es_primo(num, n + 1)    #    FUNCION RECURSIVA
    else:
        print("No es primo", n, "es divisor")
        return False
es_primo(17)
#CORTÍSMA EST0S PRIMOS

n = 17
for i in range(2, n // 2):
    if n % i == 0:
        print("It's not prime")
        break
else:
    print('Yeah! We have a prime number')"""


#usando _ si usamos rango no como una variable numérica
for _ in range(3):
    print('Repeat me 3 times!')

#for anidados - Tablas
for i in range(1, 4):
    for j in range(1, 6):
        print(f'{j} x {i} = {j*i} ')