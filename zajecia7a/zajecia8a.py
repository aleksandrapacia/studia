from random import randint
a = randint(0,99)
print(a)


def filter_for(lista):
    wynik = []
    for i in lista:
        if i % 2 == 0:
            wynik.append(i)


lista = []
for _ in range(100_000):
    lista.append(randint(1, 100))

lista = [randint(1, 100) for _ in range(100)]


def filter_for(lista):
    wynik = []
    for i in lista:
        if i % 2 == 0:
            wynik.append(i)


def filter_comprehension(lista):
    return [o for o in lista if o % 2 == 0]


def filter_lambda(lista):
    # odfiltrujemy wartosci patrzyszte
    # def odsiewaj(x):
    #     return x  % 2 == 0 # fałsz lub prawda
    #
    # return filter(odsiewaj, lista)
    return filter(lambda a: a % 2 == 0, lista)


from time import perf_counter
if __name__ == '__main__':
    #a = randint(0, 99)
    #print(a)
    #elementy = randint(0,100000000)


    # kiedy zaczynamy
    #czas_start = perf_counter()
    #wynik = filter_for(lista)
    #wynik2 = filter_comprehension(lista)
    # kiedy konczymy
    czas_end = perf_counter()
    funkcje = [filter_lambda, filter_for, filter_comprehension]
    for funkcja in funkcje:
        czas_start = perf_counter()
        wynik = funkcja(lista)
        czas_end =  perf_counter()
        print(f"Czas trwania funkcji {funkcja.__name__} wynosi {czas_end - czas_start}")



