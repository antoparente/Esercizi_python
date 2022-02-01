import os

num = input('Inserire un numero: ')

try:
    n = int(num)
except ValueError:
    print('Inserire un valore intero')
    os._exit(1)

i = 0
while i < n:
    print('*', end = '')
    i = i + 1
print('\nFinito')