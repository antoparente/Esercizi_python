import os

def vendi_libri(x, array, lista):
    if x in array and array[x] > 1:
        array[x] = array[x] - 1
        print('La vendita ha avuto successo!')
        return True
    elif x in array and array[x] <= 1:
        #try:
        del array[x]
        print('La vendita ha avuto successo!')
        return True
    else: 
        lista.append(x)
        print('Il libro e\' da ordinare!')
        return False

ordinare = list()
libri = dict()
libri = {'Harry Potter':5, 'Il signore degli anelli':7, 'IT':3, 'Cars':1,'Alla ricerca di Nemo':1,'Iron man':2,'La teoria delle pseudoscienze':20,'La vita di Pi':8,'Manuale della patente A e B':26}

c = 2
while c != 1:
    c = input('Inserire il numero 2 se si vuole proseguire, altrimenti inserire 1 --> ')
    if int(c) == 1: 
        os._exit(1)
    else: 
        libro = input('Inserisci il titolo del libro ')
        vendi_libri(libro, libri, ordinare)
        print(libri)
        print(ordinare)

    
