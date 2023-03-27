# ========================== Zadanie 1 ==========================
# A = {1/x: x∈[1,10]}
# B = {1, 2, 4, 8,…, }
# C = {x: x∈ B i x jest liczbą podzielną przez 4}

print("Zadanie 1\n")

A = {1/x for x in range(1,11)}

B = {2 ** z for z in range(11)}

C = {x for x in B if x % 4 == 0}

print("Zbiór A: ", A)
print("Zbiór B: ", B)
print("Zbiór C: ", C)

A1 = [1/x for x in range(1,11)]

B1 = [2 ** z for z in range(11)]

C1 = [x for x in B if x % 4 == 0]

print("Lista uporządkowana A: ", A1)
print("Lista uporządkowana B: ", B1)
print("Lista uporządkowana C: ", C1)

# ========================== Zadanie 2 ==========================
print("\nZadanie 2\n")

import random

macierz = [[random.randint(0,10) for i in range(4)] for i in range(4)]
print(macierz)

diagon = [macierz[i][j] for i in range(len(macierz)) for j in range(len(macierz)) if i==j]
print(diagon)

# ========================== Zadanie 3 ==========================
print("\nZadanie 3\n")

zdanie = input("wpisz zdanie: ")
lista_wyrazow = zdanie.split()

print("\nSposób 1 - list comprehension\n")
u_char = [(lista_wyrazow[i], [ord(l) if l.isascii() else chr(l) for l in lista_wyrazow[i]]) for i in range(len(lista_wyrazow))]
print(u_char)

print("\nSposób 2- generator\n")
generator = ((wyraz, [ord(l) if l.isascii() else chr(l) for l in wyraz]) for wyraz in lista_wyrazow)
for element in generator:
    print(element)

# ========================== Zadanie 4 ==========================
import math

print("\nZadanie 4\n")

def row_kwadratowe(a: int, b: int, c: int) -> (int, int):
    delta = b**2 - 4 * a * c
    if (delta < 0):
        # brak pierwiastków
        return -1
    elif (delta == 0):
        # jeden pierwiastek
        x = (-b) / (2 * a)
        return x
    else:
        # równanie ma dwa pierwiastki
        x1 = (- b - math.sqrt(delta)) / (2 * a)
        x2 = (- b + math.sqrt(delta)) / (2 * a)
        return x1, x2

print(row_kwadratowe(6,1,3))
print(row_kwadratowe(1,2,1))
print(row_kwadratowe(1,4,1))

# ========================== Zadanie 5 ==========================
print("\nZadanie 5\n")
def dice() -> [()]:
    n = int(input("podaj ilość rzutów: "))
    wynik_rzut = [(f'oczka: {random.randint(1,6)}', f'rzutów: {i}') for i in range(1,n+1)]
    print(wynik_rzut)

dice()

# ========================== Zadanie 6 ==========================
print("\nZadanie 6\n")
def zad_6(* str):
    return sorted(str)

print(zad_6('c','z','k'))

# ========================== Zadanie 7 ==========================
print("\nZadanie 7\n")
def zadanie7(** mecze):
    suma = 0
    for druzyny,punkty in mecze.items():
        suma += punkty

    return suma

zad = zadanie7(druzyna1=20, druzyna2=6)
print(zad)

