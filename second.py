"""ZBIORY"""
# # my_set = {} # Źle
# # print(type(my_set))
# # my_set = set()
# # print(type(my_set))
# my_set = {22,223,223}
# print(type(my_set))
# # add -> kolejność wymieszana
# my_set.add("Zosia")
# my_set.add("Arek")
# print(my_set)
# my_set.update({"Władka",1,2,3, True, False, 5, 10, 15})
# print(my_set)
# my_set.add(0)
# print(my_set)
# print(0 in my_set)
# #USUWANIE
# my_set.remove("Arek")
# print(my_set)
# #my_set.remove("Arek") # Wywali błąd
# my_set.discard("Arek") # tutaj nie ma błędu
# print(my_set)
# my_set.clear()
# print(my_set)

# my_set = {1,2,3,4,5}
# big_set = {0,1,2,3,4,5,6,7,8,9}

# print(my_set.issubset(big_set))
# print(my_set.issuperset(big_set))
# # Dodawanie zbiorów
# print(my_set|big_set)
# # Częśc wspólna
# print(my_set & big_set)
# # Odejmowanie 
# print(my_set - big_set)
# # Suma dwóch zbiorów bez części wspólnej
# print(my_set ^ big_set)
# # Usunięcie powtórzeń ze zbioru danych
# zbior =["Adam", "Klemens", "Lotek","Boras", "Adam"]
# jako_zbior = set(zbior)
# print(list(jako_zbior))

"""SŁOWNIKI"""
my_dict = {}
print(type(my_dict))
my_dict = dict()
student = {"imie":"Grzegorz", "nazwisko":"Brzęczyszczykiewicz", "id":3343}
# klucz : wartość
print(student["imie"])
print(student["nazwisko"])
print(student["id"])

student["oceny"] = [3,5,4]
print(student)

student["rodzice"] = {"mama":"Elizabeth", "tata":"Tomasso"}
print(student)
                        
# lista dwoch studentów
lista = []

student["imie"] = "Grzegorz"#input("Podaj imie: ")
student["nazwisko"] = "Brzeczyszcyzkiewicz"#input("Podaj nazwisko: ")
student["id"] = 343224 #input("Podaj id: ")
lista.append(student)


student["imie"] = "Franek" #input("Podaj imie: ")
student["nazwisko"] = "Krupa"#input("Podaj nazwisko: ")
student["id"] = 343434#input("Podaj id: ")


lista.append(student)
print(lista)
# OPERATOR IN SPRAWDZA TYLKO W KLUCZACH !!!
print(student.keys())
print("id" in student)
print("Franek" in student)
print("Franek" in student.values())

print(student.items()) # krotki -> klucz : wartosc
lista_krotek = list(student.items())
print(lista_krotek)
krotka = lista_krotek[0]
print(krotka[0])
print(krotka[1])
klucz, wartosc = krotka
print(klucz)
print(krotka)
# mutowalne - przekazywany adres w pamięci
print(student.values())

"""FUNKCJE"""
lista = [1,2,3,4]
krotka = (1,2,3,4)
zbior = {1,2,3,4}
suma_lista = sum(lista)
suma_krotka = sum(krotka)
suma_zbior = sum(zbior)
srednia_lista=  suma_lista/len(lista)
srednia_krotka=  suma_krotka/len(krotka)
srednia_zbior=  suma_zbior/len(zbior)
print(srednia_lista)

maxi = max(lista)
mini = min(lista)