def pieron(x):
    wynik = x /2

    for _ in range(7):
        wynik = (1/2) * (wynik + (x/wynik))
    return wynik
# wartosc domyslna
def sqrt(x, epsilon = 1e-12):
    wynik  = x / 2
    while True:
        wynik = (1/2)*(wynik + (x/wynik))
        #if abs(wynik**2 - x) < epsilon:
        #    break
        roznica = wynik **2 -x
        roznica =  roznica if roznica>0 else (-1)*roznica
        if roznica < epsilon:
            break
    return wynik

def maksimum(*args):
    #najwiekszy = max(args)
    naj = args[0]
    for i in args:
        naj = i if i >naj else naj
    return naj
# argumenty nazwane : c = 34 (**) - pakuja obiekty nazwane do jednego wspolnego obiektudef inwers():
def inwers(**kwargs):
    print(kwargs)
    print(type(kwargs))
    new_dictionary = {v: k for k, v in kwargs.items()}
    # sposob 2
    wynik  = dict()
    for klucz, wartosc in kwargs.items():
        wynik[wartosc] = klucz
        return wynik
    return new_dictionary
# NAPISZ FUNKCJE NA MEDIANE !!!

# szukamy wartosc maksymalna
def maksss(*args, **kwargs):
    print(args)
    print(kwargs)
    lista  = list(args)  + list(kwargs.values())
    maks = lista[0]
    for i in lista:
        maks = i if i > maks else maks
    return maks
#argumenty pozycyjne - wprowadzane po przecinku
if __name__ == '__main__':
    print(pieron(9))
    print(maksimum(124,56454,54,5645,54))
    print(maksimum(221,54))
    print(maksimum(3,2,4,6,4,2,54,7,4,23,46))

    print(inwers(imie = "Rafal", naziwkso = 'Kocierz'))
    #---> slownik {"Rafal":"imie", "Kocierz":"naziwkso"}
    print(maksss(1,2,3,534,21,c=121, d=765))


#TODO: ZADANIE DOMOWE ---> odsiej na różne sposoby
def filter_for(lista):
    wynik = []
    for i in lista:
        if i % 2 == 0:
            wynik.append(i)
def filter_comprehension(lista):
    return [o for o in lista if o  % 2 == 0 ]
def filter_lambda(lista):
    # odfiltrujemy wartosci patrzyszte
    # def odsiewaj(x):
    #     return x  % 2 == 0 # fałsz lub prawda
    #
    # return filter(odsiewaj, lista)
    return filter(lambda a : a %2 ==0 , lista)

def kwadrat_for(lista):
    wynik=[]
    for i in lista:
        wynik.append(i**2)
def kwadrat_comprehension(lista):
    return [i **2 for i in lista]
def kwadrat_map(lista):
    return list(map(lambda a : a **2 , lista))

