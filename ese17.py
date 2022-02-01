import math
import os
 
n1 = input('Inserire primo numero intero: ')
try:
    x1 = int(n1)
except ValueError:
    print("Non e\' un intero!")
    os._exit(1)
 
n2 = input('Inserire secondo numero intero: ')
try:
    x2 = int(n2)
except ValueError:
    print("Non e\' un intero!")
    os._exit(1)
    
n3 = input('Inserire terzo numero intero: ')
try:
    x3 = int(n3)
except ValueError:
    print("Non e\' un intero!")
    os._exit(1)

if x1 > x2:
    if x1 > x3:
        print('Maggiore: ' + str(x1))
    else:
        print('Maggiore: ' + str(x3))
else: 
    if x2 > x3:
        print('Maggiore: ' + str(x2))
    else:
        print('Maggiore: ' + str(x3))

if x1 < x2:
    if x1 < x3:
        print('Minore: ' + str(x1))
    else:
        print('Minore: ' + str(x3))
else:
    if x2 < x3:
        print('Minore: ' + str(x2))
    else:
        print('Minore: ' + str(x3))

media = (x1 + x2 + x3) / 3
print('Media aritemetica: ' + str(media))
somma = x1 + x2 + x3

if somma > 0:
    rad = math.sqrt(int(somma))
    print('Radice della somma: ' + str(rad))
else:
    print('La somma non e\' > 0!')


