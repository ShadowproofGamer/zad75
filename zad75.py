slownik = {}
for i in range(97, 123):
    slownik[chr(i)] = (i-97)
#print(slownik)

def podstawienie(litera, A, B):
    temp = slownik[litera]*A+B
    if temp>25:
        temp%=26
        #print(chr(temp+97))
    return chr(temp+97)

def szyfrowanie(slowo, A, B):
    slowo_szyfr = ''
    for i in slowo:
        slowo_szyfr+=podstawienie(i, A, B)
    return slowo_szyfr

def deszyfrowanie(slowo_szyfr, A, B):
    slowo = ''
    for i in slowo_szyfr:
        slowo+=podstawienie(i, A, B)
    return slowo

def znajdowanie_klucza(slowo1, slowo2):
    slowo1_len = len(slowo1)
    slowo2_len = len(slowo2)
    for A in range(0, 26):
        for B in range(0, 26):
            if podstawienie(slowo2[0], A, B) == slowo1[0] and podstawienie(slowo2[1], A, B) == slowo1[1] and podstawienie(slowo2[2], A, B) == slowo1[2] and podstawienie(slowo2[slowo2_len-1], A, B) == slowo1[slowo1_len-1]:
                print('klucz deszyfrujacy: A=', A, 'B=',  B)
            elif podstawienie(slowo1[0], A, B) == slowo2[0] and podstawienie(slowo1[1], A, B) == slowo2[1] and podstawienie(slowo1[2], A, B) == slowo2[2] and podstawienie(slowo1[slowo1_len-1], A, B) == slowo2[slowo2_len-1]:
                print('klucz szyfrujacy: A=', A, 'B=', B)

plik=open('tekst.txt')
dane=plik.read().split()
print('punkt1:')
for i in dane:
    if i[0]==i[len(i)-1]:
        print(i)

print("punkt2:")
for j in dane:
    if len(j)>=10:
        print(szyfrowanie(j, 5, 2))

print("punkt3:")
plik.close()
plik2=open('probka.txt')
dane2=plik2.read().split()
for k in range(0, len(dane2), 2):
    print(dane2[k], dane2[k+1])
    znajdowanie_klucza(dane2[k], dane2[k+1])