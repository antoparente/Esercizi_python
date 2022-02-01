import math
import os

n = input('Inserire un valore tra 1 e 12(mese): ')

try: 
    mese = int(n)
except ValueError:
    print('Non è un numero intero!')
    os._exit(1)

if mese < 1 or mese > 12:
    print('Inserire un valore che sia compreso tra 1 e 12!')
    os._exit(1)

if mese <= 3 and mese == 12:
    print('Stagione: Inverno')

if mese > 3 and mese <= 6:
    print('Stagione: Primavera')
    
if mese > 6 and mese <= 9:
    print('Stagione: Estate') 

if mese > 9 and mese < 12:
    print('Stagione: Autunno') 