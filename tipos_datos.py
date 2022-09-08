#años bisiestos si año % 4 == 0 y año % 100 != 0
lista = []
x = 0
for i in range (1900, 2000, 4):
    if i % 4 == 0 and i % 100 != 0:  
        print(i)

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