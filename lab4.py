#zad1 Wygeneruj liczby podzielne przez 4 i zapisz je do pliku.
import random
liczby = []
i = 0

while i < 10:
    los = random.randint(0, 1024)
    if los % 4 == 0:
        liczby.append(los)
        i += 1
plik = open('plik.txt', 'a')
for x in liczby:
    plik.write(str(x) +  '\n')
plik.close()

#zad2 Odczytaj plik z poprzedniego zadania i wyświetl jego zawartość
file = open('plik.txt', "r")
for linia in file:
    print(linia)
file.close()
#zad3 Wykorzystując komendę with zapisz kilka linijek tekstu do pliku a następnie wyświetl je na ekranie.
#zad4
class naZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed
    def wyswietl_produkt(self):
        return self.nazwa_produktu
    def ile_produktu(self):
        return f'{self.ilosc} {self.jednostka_miary}'
    def ile_kosztuje(self):
        return self.ilosc * self.cena_jed

produkt1 = naZakupy('ziemniaki', 3, 'kg', 2)
print(produkt1.wyswietl_produkt())
print(produkt1.ile_produktu())
print(produkt1.ile_kosztuje())

#zad5
#zad6
class Robaczek:
    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok

    def idz_w_gore(self, ile_krokow):
        self.y += ile_krokow * self.krok

    def idz_w_dol(self, ile_krokow):
        self.y -= ile_krokow * self.krok

    def idz_w_lewo(self, ile_krokow):
        self.x -= ile_krokow * self.krok

    def idz_w_prawo(self, ile_krokow):
        self.x += ile_krokow * self.krok

    def pokaz_gdzie_jestes(self):
        return f'({self.x}, {self.y})'


robak = Robaczek(0, 0, 1)

robak.idz_w_lewo(10)
robak.idz_w_prawo(10)
robak.idz_w_gore(1)
robak.idz_w_dol(100)
print(robak.pokaz_gdzie_jestes())