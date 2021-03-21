import sys
from math import sqrt
#Zad1
lista = ['Koszykówka', 'Siatkówka', 'Skoki Narciarskie']
lista.reverse()
print(lista)
lista.append('Piłka Ręczna')
lista.append('Hokej')
print(lista)
#Zad2
slowa = {'cr':'co robisz', 'zw':'zaraz wracam', 'jj':'juz jestem', 'cb':'ciebie'}
print(slowa)
#Zad3
games = {'Valheim':'Sandbox', 'World of Warcraft':'MMORPG', 'Call of Duty':'FPS'}
print(games)
print(len(games))
#Zad4
zdanie = input('Wpisz zdanie: ')
print('Liczba \'a\' w zdaniu \'{}\': {}'.format(zdanie, zdanie.count('a')))
#Zad5
sys.stdout.write('Podaj trzy liczby całkowite: ')
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
wynik = a ** b + c
sys.stdout.write('a ^ b + c = %s' % wynik)
#Zad6
a = int(input('Podaj a: '))
b = int(input('Podaj b: '))
c = int(input('Podaj c: '))
if a >= b:
    if a >= c:
        print('Największa liczba: %d' % a)
    else:
        print('Największa liczba: %d' % c)
elif b >= c:
    print('Największa liczba: %d' % b)
else:
    print('Największa liczba: %d' % c)
#Zad7
liczby = [1, 2, 3, 4.8, 5.23, 6.88]
for l in liczby:
    print(l * l)
#Zad8
parzyste = []
i = 0
while i < 10:
    dodawana_liczba = int(input('Podaj liczbę: '))
    if dodawana_liczba % 2 == 0:
        parzyste.append(dodawana_liczba)
    i += 1
print(parzyste)
#Zad10
pierwiastek = int(input('Podaj liczbe: '))
if pierwiastek < 0:
        print('Liczba nie moze byc ujemna')
print(sqrt(pierwiastek))