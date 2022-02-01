import math
x1 = input('Inserire x1: ')
x2 = input('Inserire x2: ')
print('Primo punto: (' + str(x1) +', ' + str(x2) + ')')
y1 = input('Inserire y1: ')
y2 = input('Inserire y2: ')
print('Secondo punto: (' + str(y1) +', ' + str(y2) + ')')
dis = math.sqrt(pow(int(x1) - int(x2), 2) + pow(int(y1) - int(y2), 2))
print('Distanza Euclidea: ' + str(dis))