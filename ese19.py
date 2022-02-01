import math
import os

n = input('Inserire mese (valore tra 1e 12): ')

try: 
    mese = int(n)
except ValueError:
    print('Non è un numero intero!')
    os._exit(1)

if mese < 1 or mese > 12:
    print('Inserire un valore che sia compreso tra 1 e 12!')
    os._exit(1)

gg = input('Inserire valore del giorno: ')

try: 
    giorno = int(gg)
except ValueError:
    print('Non è un numero intero!')
    os._exit(1)
if giorno <= 0:
    print('Inserire un giorno possibile!')
    

if ((mese == 4 or mese == 6 or mese == 9 or mese == 11) and giorno > 30) or  (mese == 2 and giorno > 28) or  ((mese == 1 or mese == 3 or mese == 5 or mese ==  7 or mese == 8 or mese == 10 or mese == 12) and giorno > 31):
    print('Giorno non disponibile in questo mese!')
    os._exit(1)

if mese == 3 or mese == 12:
    if mese == 3 and giorno > 20:
        print('Primavera')
    elif mese == 3 and giorno <= 20:
        print('Inverno')
    elif mese == 12 and giorno < 21:
        print('Autunno')
    elif mese == 12 and giorno >= 21:
        print('Inverno')
        
elif mese == 6 or mese == 9:
    if mese == 6 and  giorno < 21:
        print('Primavera')
    elif mese == 6 and  giorno >= 21:
        print('Estate')
    elif mese == 9 and giorno <= 22:
        print('Estate')
    elif  mese == 9 and giorno > 22:
        print('Autunno')
        
elif mese == 7 or mese == 8:
    print('Estate')
        
elif mese == 4 or mese == 5:
    print('Primavera')
    
elif mese == 10 or mese == 11:
    print('Autunno')
    
elif mese == 1 or mese == 2:
    print('Inverno')
