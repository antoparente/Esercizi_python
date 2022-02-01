while True:
    alt = input('Altezza: ')
    try: 
        h = int(alt)
    except ValueError:
        pass
    if h > 0 or h <= 9:
        break;

cont = 0 
for riga in range(1, h + 1):
    for colonna in range(1, h - riga + 1):
        print(' ', end='')
    
    cont = 1
    for j in range(h - riga + 1, h + 1):
        print(str(cont), end='')
        cont = cont + 1
    cont = riga - 1 
    for j in range(h - riga + 2, h + 1):
        print(str(cont), end='')
        cont = cont - 1
    print('\n', end='')