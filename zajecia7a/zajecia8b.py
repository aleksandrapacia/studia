# Klasa ulamki
# musi umiec sie przedstawic czyli print
# musimy umiec dodac ulamki
# musimy umiec mnozyc ulamki

# Co musi przechowywac?????
# Klasa nie żyje ; trzeba stworzyc obiekt
class Ulamek():
    # kontruktor - cos co uruchamia sie automatycznie gdy obiekt jest tworzony
    def __init__(self, mianownik, licznik ):
        # sa lokalne, wiec musimy je utrwalic  // l i m to pola
        self.m=mianownik
        self.l=licznik

ulamek1 = Ulamek(1,2)
ulamek2 = Ulamek(2, 4)
print(ulamek1.m)
print(ulamek1.l)
ulamek1.l = 3
print(ulamek1.l)
print(ulamek1) #objekt w miejscu pamieci