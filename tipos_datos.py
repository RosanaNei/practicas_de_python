#años bisiestos si año % 4 == 0 y año % 100 != 0
""" lista = []
x = 0
for i in range (1900, 2000, 4):
    if i % 4 == 0 and i % 100 != 0:  
        print(i) """

value = None
if value is None:
    print(	'Value is clearly None'	)
else:
    #valuepodríacontenerTrue,False(uotro)
    print(	'Value has some useful value')
    
value = 99
if value is not None:
    print(f'{value=}')
    
print((123025369547457).bit_length())
print(bin(999))
print(hex(999))

#DIVMOD (fc builtin)
def modulo (x, y):
    return x % y
def floor_division (x, y):
    return x // y
def metodo_divmod(x, y):
    return divmod(x, y)
print(modulo(11, 2), floor_division(11, 2), divmod (11, 2),', divmod es un método que entrega el modulo y la floor division')

x = round(100.96,-2)
z = int(100.96)
y = round(100.967893, 4)
t = 1.75.as_integer_ratio() #devuelve la frccion que corresponde a un float, en este caso es 7/4
lista = [x, z, y, t]
for num in lista:
    print(num)
    
