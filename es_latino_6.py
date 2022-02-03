import json

try:
    dati = json.load(open('file4.json'))
except IOError:
    print('Errore nell\'apertura del file!')
    os._exit(1)
    
lista = list()
for i in range(0, len(dati)):
    lista = lista + dati[i]
print(lista)

lista_copia = list()

flag = False
for i in range (0, len(lista)):
    flag = False
    for j in range (0, len(lista_copia)):
        if(lista[i] == lista_copia[j]):
            flag = True
    if flag == False:
        lista_copia.append(lista[i])

print(lista_copia)

lista_copia2 = list(lista_copia)
listone = list()

simbolo1 = lista_copia[0]
print(listone)


for i in range (0, len(lista_copia)): 
    listone.append([])
    for j in range (1, len(lista_copia)+1):
        if j == 1:
            pri = lista_copia[0]   
            print(pri)
        if j != len(lista_copia):
            lista_copia[j - 1] = lista_copia[j]
            listone[i].append(lista_copia[j-1])
        else:
            lista_copia[j-1] = pri
            listone[i].append(lista_copia[j-1])
            print(lista_copia)             

print(listone)
