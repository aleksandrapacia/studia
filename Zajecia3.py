# O Krotkach
# cos = "Rafal", "Wredny", "Jest"
# print(cos)
# print(type(cos))
# cos = ("rafal", "wredny", "jest")
# a = 10
# b = 20
# c = a,b
# print(c)
# auto = ("CX5", "Mazda", 2024)
# print(auto.index("CX5")) # wyswietla index
# #model  = auto[0]
# #marka = auto[1]
# #rocznik = auto[2]

# # rozpakowanie krotki
# (model, marka, rocznik) =("CX5", "Mazda", 2024)
# print(f"Model: {model}")
# print(f"Marka: {marka}")
# print(f"Rok: {rocznik}")

# a = 10
# b = 15
# print(a)
# print(b)
# (a, b) = (10, 15)
# a, b = 10, 15

# # METODY
# print("ilosc", auto.count("Mazda"))
# print(dir(auto))
# c = 2 
# print(dir(3))
# print("\n")

# c  = 2 + 2
# # dodawanie
# print((3).__add__(2))
# # odejmowanie
# print((3).__sub__(2))
# # mnozenie
# print((3).__mul__(2))
# # dzielenie 
# print((4).__truediv__(2))
# # potegowanie
# print((4).__pow__(2))
# # divmode: (wynik dzielenia calkowitego, reszta z dzielenia)
# print((5).__divmod__(3))

# CIĄGI ZNAKÓW
zoo = [["Skid", "Micek", "Flora"],  [1000,5000,6000],  [10,500,560]]
print(zoo)

# Nazwa zwierzaka     Cena    Dlugosc zycia
# Skid                1000     10
# Micek               5000     500
# Flora               6000     560

# print("Tekst".ljust(20))
# print("Tekst".center(20))
# print("Tekst".rjust(20))



# print("Nazwa".ljust(20))
# print("Cena".center(20))
# print(zoo[0][0].ljust(20))
# print(zoo[0][1].ljust(20))
# print(zoo[0][2].ljust(20))

# print("Cena".center(20))
# print(str(zoo[1][0]).center(20))
# print(str(zoo[1][1]).center(20))
# print(str(zoo[1][2]).center(20))

# print("Dlugosc zycia".rjust(20))
# print(str(zoo[2][0]).rjust(20))
# print(str(zoo[2][1]).rjust(20))
# print(str(zoo[2][2]).rjust(20))

linia = "Nazwa zwierzaka".rjust(20)+"Cena".center(15)+"Dlugosc zycia".ljust(20)
print(linia)
print(zoo[0][0].ljust(20), str(zoo[1][0]).center(15), str(zoo[2][0]).rjust(20), sep="")
a=1
print(zoo[0][a].ljust(20), str(zoo[1][a]).center(15), str(zoo[2][a]).rjust(20), sep="")
a=2 
print(zoo[0][a].ljust(20), str(zoo[1][a]).center(15), str(zoo[2][a]).rjust(20), sep="")

# funkcja split()
tekst = "Ola Pacia   2.5 3.5 4.0"
print(tekst.split())
slowa = tekst.split()
imie = slowa[0]
print("imie:", imie)
nazwisko = slowa[1]
ocena1 = slowa[2]
ocena2 = slowa[3]
ocena3 = slowa[4]
print("nazwisko:",nazwisko)
print("oceny:")
print(ocena1)
print(ocena2)
print(ocena3)
rozdziel = tekst.split()
nowy_str = " ".join(rozdziel)
print(nowy_str)

# upper , lower 
text = "Ola lubi koty"
print(text.lower())
print(text.upper())