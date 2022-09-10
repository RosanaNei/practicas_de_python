""" slayer=["Buffy", "Anne", "Summers"] 
print(" ".join(slayer))
print('-v-'.join(slayer))
 """

#Método SPLIT
# #Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con 
#cada palabra que contiene y la cantidad de veces que aparece (frecuencia). 
def count_words(text):
    text = text.split()
    words = {}
    for i in text:
        if i in words:
            words[i] += 1
        else:
            words[i] = 1
    return words

text = 'estoy la recontra  la perdida la en esto'
print(count_words(text))
