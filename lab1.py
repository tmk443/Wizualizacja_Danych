
#zadanie1
print("Zadanie 1")
a = 5 #integer
b = 6.4 #float
c =  'Ala ma kota' #string
print(type(a))
print(type(b))
print(type(c))
print("================================================")
#zadanie2
print("Zadanie 2")
liczba1 = float(input(u"Podaj pierwszą liczbę: "))
liczba2 = float(input(u"Podaj drugą liczbę: "))
dzialanie = input(u"Wybierz działanie: \n"
                  u"1. Dodawanie\n"
                  u"2. Odejmowanie\n"
                  u"3. Mnożenie\n"
                  u"4. Dzielenie\n")
if dzialanie == "1":
    print("Wynik: ",liczba1 + liczba2)
elif dzialanie == "2":
    print("Wynik: ",liczba1 - liczba2)
elif dzialanie == "3":
    print("Wynik: ",liczba1 * liczba2)
elif dzialanie == "4":
    print("Wynik: ",liczba1 / liczba2)
print("================================================")
#zadanie3
print("Zadanie 3")
d = 0
print(d)
d+=1
print(d)
d*=2
print(d)
d-=3
print(d)
d/=4
print(d)
d**=5
print(d)
d%=6
print(d)
print("================================================")
#zadanie4
print("Zadanie 4")
e = 2.7182
pow(e,10)
print(e)
print("================================================")
#zadanie5
print("Zadanie 5")
imie = 'TOMASZ'
nazwisko = 'MASTYKA'
print(imie.capitalize() +" "+ nazwisko.capitalize())
print("================================================")
#zadanie6
print("Zadanie 6")
tekst = """Tyle było dni
Do utraty sił
Do utraty tchu
Tyle było chwil"""
ilosc = tekst.count("utraty")
print("Ilość słów `utraty`: ",ilosc)
print("================================================")
#zadanie7
print("Zadanie 7")
slowo = "książka"
print(slowo[1]+" "+ slowo[len(slowo)-1])
print("================================================")
#zadanie8
print("Zadanie 8")
print(tekst.split())
print("================================================")
