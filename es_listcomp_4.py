cubi = [n**3 for n in range(10)]
print(cubi)

def funPari(x):
    if x % 2 == 0:
        return True
    else:
        return False

pari = filter(funPari, cubi)
pari2 = list(pari)
print(pari2)

def molt (a):
    return a*3

moltip = map(molt, pari2)
print(list(moltip))