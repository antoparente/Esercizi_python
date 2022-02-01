import os

while True:                                                                         
    num = input('Inserire un numero: ')     
    flag = True
    try:
        n = int(num)
    except ValueError:
        print(num + 'non e\' un valore intero')
        flag = False
    if flag:
        break

i = 0
while i < n:
    print('*', end = '')
    i = i + 1
print('\nFinito')