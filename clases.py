class StarWarsDroid:
    pass
#instancias de clase
c3po = StarWarsDroid()
r2d2 = StarWarsDroid()
bb8 = StarWarsDroid()

print(type(c3po))

#AÑADIENDO ATRIBUTOS Un atributo no es más que una variable, un nombre al que asignamos un valor, 
# con la particularidad de vivir dentro de una clase o de un objeto.Los atributos – por lo general – 
# se suelen asignar durante la creación de un objeto, pero también es posible añadirlos a posteriori:
blue_droid = StarWarsDroid()
golden_droid = StarWarsDroid()

golden_droid.name = 'C-3PO'

blue_droid.name = 'R2-D2'
blue_droid.height = 1.09
blue_droid.num_feet = 3
blue_droid.partner_droid = golden_droid  # otro droide como atributo
print(type(blue_droid.partner_droid), blue_droid.name )
blue_droid.partner_droid.num_feet = 8
print(blue_droid.partner_droid.num_feet)

#AÑADIENDO METODOS Añadiendo métodos. Un método es una función que forma parte de una clase o de un objeto. 
# En su ámbito tiene acceso a otros métodos y atributos de la clase o del objeto al que pertenece.La definición 
# de un método (de instancia) es análoga a la de una función ordinaria, pero incorporando un primer parámetro 
# self que hace referencia a la instancia actual del objeto.

class Droid:
    def switch_on(self):
        print("Hi! I'm a droid. Can I help you?")

    def switch_off(self):
        print("Bye! I'm going to sleep")

k2so = Droid()
k2so.switch_on()
k2so.switch_off()

#METODO CONSTRUCTOR def__init__

class Droid:
    def __init__(self, pname):
        self.name = pname
        
droid = Droid('BB-8')
print(droid.name)

class MobilePhone: 
    def __init__(self, pmanufacturer, pscreen_size, pnum_cores):
        self.manufacturer = pmanufacturer
        self.screen_size = pscreen_size
        self.num_cors = pnum_cores
        self.status = 0
        self.apps = []

    def power_on(self):
        self.status = 1

    def power_off(self):
        self.status = 0

    def install_app(self, *app):
        self.apps.append(app)

    def uninstall_app(self, apps):
        for app in apps:
            self.apps.remove(app)
 
huawei = MobilePhone('Huawei', 5.3, 8)
huawei.power_on()
print(huawei.status)
huawei.install_app('Twitter', 'coso') 
print(huawei.apps)
#huawei.uninstall_app('Twitter')
#print(huawei.apps) aca me tira error
huawei.power_off()
print(huawei.status)

#modificacion de un atributo previamente declarado
class Droid:
    def __init__(self, name):
        self.name = name
        
droid = Droid('C-3PO')
print(droid.name)
droid.name = 'waka-waka'  # esto sería válido!
print(droid.name)
print('\n')

#PROPIEDADES - los atributos definidos en un objeto son accesibles públicamente. para la privacidad de los atributos 
# es el uso de propiedades. La forma más común de aplicar propiedades es mediante el uso de decoradores: 
# @property para leer el valor de un atributo.
# @name.setter para escribir el valor de un atributo.
class Droid:
    def __init__(self, name):
        self.hidden_name = name

    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name

    @name.setter
    def name(self, name):
        print('inside the setter')
        self.hidden_name = name
        return self.hidden_name

droid = Droid('N1-G3L')
print(droid.name)
droid.name = 'Nigel'
print(droid.name)

#VALORES CALCULADOS
class AstromechDroid:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    @property
    def periscope_height(self):
        return 0.3 * self.height

droid = AstromechDroid('R2-D2', 1.05)
droid.periscope_height  # podemos acceder como atributo
#droid.periscope_height = 10  # no podemos modificarlo TIRA ERROR

#ATRIBUTOS OCULTOS Python tiene una convención sobre aquellos atributos que queremos hacer «privados» (u ocultos): 
# comenzar el  nombre con doble subguión __ aquellos atributos que queremos hacer «privados» (u ocultos): comenzar 
# el nombre con doble subguión __
class Droid:
    def __init__(self, name):
        self.__name = name

droid = Droid('BC-44')
#print(f'Este es el nombre:{droid.__name}')  # efectivamente no aparece como atributo tira error 
#AttributeError: 'Droid' object has no attribute '__name'
#Para acceder al valor del atributo supuestamente privado, hay que modificar el nombre del atributo incorporando 
# la clase como un prefijo. 
print(droid._Droid__name)

#ATRIBUTOS DE CLASEPodemos asignar atributos a las clases y serán heredados por todos los objetos instanciados de 
# esa clase.










