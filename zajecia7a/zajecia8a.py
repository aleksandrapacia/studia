from random import randint
a = randint(0,99)
print(a)

from time import perf_counter
if __name__ == '__main__':
    #a = randint(0, 99)
    #print(a)
    #elementy = randint(0,100000000)
    def filter_for(lista):
        wynik = []
        for i in lista:
            if i % 2 == 0:
                wynik.append(i)
    lista = []
    for _ in range(100_000):
        lista.append(randint(1,100))

    lista = [randint(1,100) for _ in range(100)]
    # kiedy zaczynamy
    czas_start = perf_counter()
    wynik = filter_for(lista)
    # kiedy konczymy
    czas_end = perf_counter()
    print(f"Czas trwania filtorwania z for wynosi {czas_end-czas_start}")