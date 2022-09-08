#dos iteraciones quen hacen lo mismo, con y sin funcion continue
num = 10
while num >= 1:
    num -= 1
    if num % 3 == 0:
        continue
    print(num,end=	',' )

num = 10
while num >= 1:
    num -= 1
    if num % 3 != 0:
       print(num,end=	',' )