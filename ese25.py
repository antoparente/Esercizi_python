import math

while True:
    num = input('Inserire numero intero > di 0: ')
    try:
        n = int(num)
    except ValueError:
        print(n + ' non è un numero intero!')
    if n > 0:
        break;

list(num)

i = 0
while i < len(num):
    n = num[i]
    for lungh in range (0, int(n)):
        print('*', end='')
    i = i + 1
    print('\n', end='')