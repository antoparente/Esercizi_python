import os

l1 = input('Lato a: ')

try:
    a = int(l1)
except ValueError:
    print('Inserire un valore intero!')
    os._exit(1)

if a <= 0:
    print('Inserire un valore >  di 0!')
    os._exit(1)

l2 = input('Lato b: ')

try:
    b = int(l2)
except ValueError:
    print('Inserire un valore intero!')
    os._exit(1)

if b <= 0:
    print('Inserire un valore >  di 0!')
    os._exit(1)

for riga in range(0, b):
    if riga == 0 or riga == (b - 1):
        for colonna in range(0, a):
            print('* ', end='')
        print('\n', end='')
    else: 
        for colonna in range(0, a):
            if colonna == 0 or colonna == (a - 1):
                print('* ', end='')
            else: 
                print('  ', end='')
        print('\n', end='')