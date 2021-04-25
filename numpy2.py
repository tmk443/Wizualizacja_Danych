import numpy as np
from math import *

# Zadanie 1: Utwórz dwie macierze 1x3 różnych wartości a następnie wykonaj operację mnożenia.

a = np.array([6, 4, 11])
b = np.array([5, 5, 20])
print(a * 5)
print(b * 9)

# Zadanie 2: Utwórz macierz 3x3 oraz 4x4 i znajdź najniższe wartości dla każdej kolumny i każdego rzędu.

a = np.arange(9).reshape(3, 3)
print(a)
b = np.arange(16).reshape(4, 4)
print(b)

print(a.min(axis=1))
print(a.min(axis=0))
print(b.min(axis=1))
print(b.min(axis=0))

# zadanie 3: Wykorzystaj macierze z zadania pierwszego i wykonaj iloczyn macierzy.

a = np.array([6, 4, 11])
b = np.array([5, 5, 20]).reshape(3, 1)
print(a * b)

# Zadanie 4: Utwórz dwie macierze 1x3 gdzie pierwsza z nich będzie zawierała liczby całkowite, a druga liczby rzeczywiste. Następnie wykonaj na nich operację mnożenia.

a = np.array([7, 1, 9], dtype="int")
b = np.array([4.4, 8.6, 1.2], dtype='float')
print(a * 4)
print(b * 2)

# Zadanie 5: Utwórz macierz 2x3 różnych wartości a następnie wylicz sinus dla każdej z jej wartości i zapisz do zmiennej “a”.

x = np.array([[2, 8, 7], [5, 1, 3]])
a = np.sin(x)
print(a)

# zad 6
y = np.array([[1, 2, 3], [4, 5, 6]])
b = np.cos(y)
print(b)
# Zadanie 7: Wykonaj funkcję dodawania obu macierzy zapisanych wcześniej do zmiennych a i b.

print(a + b)

# Zadanie 8: Wygeneruj macierz 3x3 i wyświetl w pętli każdy z rzędów.

a = np.arange(9).reshape(3, 3)
for x in range(3):
    print(a[x, :])

# Zadanie 9: Wygeneruj macierz 3x3 i wyświetl w pętli każdy element korzystając z opcji “spłaszczenia” macierzy. (użyj funkcji flat())

a = np.arange(9)
for c in a.flat:
    print(c)

# Zadanie 10: Wygeneruj macierz 9x9 a następnie zmień jej kształt. Jakie mamy możliwości i dlaczego?

a = np.arange(81)


# Zadanie 11: Wygeneruj macierz płaską (wektor) i przekształć ją na macierz 3x4. Wygeneruj w ten sposób jeszcze kombinacje 4x3 i 2x6. Spłaszcz każdą z nich i wyświetl wyniki. Czy są identyczne?

a = np.arange(12)
b = a.reshape(3, 4)
c = a.reshape(4, 3)
d = a.reshape(2, 6)
print(b)
print(c)
print(d)
print(b.flatten())
print(c.flatten())
print(d.flatten())
