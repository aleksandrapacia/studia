# CTRL + /   ---> comment
# a = input("Podaj pierwsza liczbe : ")
# b = input("Dodaj druga liczbe : ")
# print(int(a)*int(b))
lista_nowa = []
lista_nowa.append('Cos')

lista_nowa.append("Polska")
lista_nowa.append("Brazylia")
lista_nowa.append("Portugalia")
lista_nowa.insert(0, "Portugalia")

lista_nowa[0] = "USA"

del lista_nowa[1]

lista_nowa.pop()

ostatnia = lista_nowa.pop()
#lista_nowa.remove('USA')

zabawnaLista = ["USA", "Polska", "Kanada", "Italy"]
#del zabawnaLista[1]
#posortowana=sorted(zabawnaLista)
posortowana_XD = sorted(zabawnaLista, reverse=True)
zabawnaLista.sort()
print(zabawnaLista.reverse())
print(zabawnaLista)
#def wyswietl():
    #print(lista_nowa)
    #print(ostatnia)
    #print(zabawnaLista)
    #print(posortowana_XD)
#wyswietl()

nowa = ["Polska", "Anglia", "Hiszpania"]
print(nowa.count("Polska"))
print(nowa.count("Hiszpania"))
print(nowa.count("Wlochy"))
print("NICOSC" in nowa)

# KROTKA 
krotka = tuple()
krotka_2  = ()
print(krotka)
print(krotka_2)
nowa_kr = tuple(nowa)
print(nowa_kr)

print(nowa_kr.index("Polska"))
print(krotka[:-1])