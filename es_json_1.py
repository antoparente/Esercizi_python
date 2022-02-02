import json
import os

try:
    dati = json.load(open('file1.json'))
except IOError:
    print('Errore nell\'apertura del file!')
    os._exit(1)
    

i = 0
a = 0
b = 0
my_list = list()
tupla = ()
for i in range(0, len(dati)):  
    '''print(dati)'''
    lst = list(dati[i])
    for j in range(0, len(lst)):
        if int(lst[j]) % 2 == 0:
            b = b + int(lst[j])
        else:
            a = a + int(lst[j])
    my_list.append('('+ str(a) + ',' + str(b) + ')')
    a = 0
    b = 0
    
tupla = tuple(my_list)
print(tupla)