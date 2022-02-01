import math
import os
 
num = input('Inserire un numero intero (> 0): ')
try:
    x = int(num)
except ValueError:
    print("Non e\' un intero!")
    os._exit(1)

if x > 0 :
    rad = math.sqrt(x)
    print('Radice quadrata: ' + str(rad))
else: 
    print("Non è  un numero > 0!")