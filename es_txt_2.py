try:
    lettura = open('ftesto10_3.txt',  'r').read()
except IOError:
    print('Errore nell\'apertura del file!')
    os._exit(1)

print(lettura)
d = dict()
i = 0
j = 0
f = list(lettura)
final = list()
stringa = ''
for i in range (0, len(f)):
    if f[i] != ' ' and f[i] != '\n':
        final.append(f[i])
print(final)

chiavi = list()
valori = list()
copia_valori = list(final)

for i in range (0, len(final)):
    if final[i] == ':':
        chiavi.append(int(final[i-1]))

for i in range (0, len(final)):
    if final[i] == ':':
        copia_valori.remove(final[i-1])

copia_valori.remove(copia_valori[0])

for i in range (0, len(copia_valori)):
    stringa = stringa + copia_valori[i]

#print(stringa)

arr = stringa.split(':')

#print(arr)

for i in range (0, len(arr)):
    li = list(arr[i])
    for j in range (0, len(li)):
        li[j] = int(li[j])
    d[chiavi[i]] = li 
        
print(d)
