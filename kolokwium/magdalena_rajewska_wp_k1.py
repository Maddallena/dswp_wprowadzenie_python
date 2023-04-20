import string
import random
import math


def zadanie_1(tekst):
    slownik = {}
    ascii_lower = 0
    ascii_upper = 0
    str_digits = 0

    for el in tekst:
        if el in string.ascii_lowercase:
            ascii_lower += 1
            slownik['lower'] = ascii_lower
        elif el in string.ascii_uppercase:
            ascii_upper += 1
            slownik['upper'] = ascii_upper
        elif el in string.digits:
            str_digits += 1
            slownik['digits'] = str_digits
    return slownik
    pass


# z1 = zadanie_1('ijiuUhiKLuKJi654685igihihf54887974')
# for s in z1:
#     print(s, z1[s])


def zadanie_2(n: int):
    ciag_znakow = input('wprowadź ciąg znaków: ')
    for c in range(n):
        print(ciag_znakow, end='')
    pass


# zadanie_2(5)


def zadanie_3():
    i = input('wpisz minimum 3 wyrazy').split()

    while len(i) < 3:
        c = input('Dodaj kolejny wyraz: ').split()
        if len(c) >= 2:
            for el in c:
                i.append(el)

    tekst = ' '.join(random.choice(i) for x in range(3))
    tekst[0].capitalize()
    print(tekst)
    pass


# zadanie_3()

def zadanie_4():
    lista = [math.log2(x**2) for x in range(1,17)]
    print(lista)
    pass
# zadanie_4()
def zadanie_5(lista_liczb):
    max_len = len(str(max(lista_liczb)))
    new_list = []
    for tmp in range(len(lista_liczb)):
        dl = str(lista_liczb[tmp])
        new_str = ''
        if len(dl) != max_len:
            ile_zer = max_len - len(dl)
            for el in range(ile_zer):
                new_str += '0'
            new_str += str(lista_liczb[tmp])
            new_list.append(new_str)
        else:
            new_list.append(dl)
    return new_list
    pass


# print(zadanie_5([1, 23, 564]))


def zadanie_6(tekst, max_ilosc_znakow):
    if tekst[max_ilosc_znakow + 1] != ' ' or tekst[max_ilosc_znakow + 1] != '.':
        ind_spacji =[l for l in range(len(tekst[:max_ilosc_znakow])) if tekst[l] == ' ']
        return tekst[:ind_spacji[-1]]
    else:
        return tekst[:max_ilosc_znakow]

print(zadanie_6('alicja w krainie czarow zna szalonego kapelusznika', 25))

#zadeklaruj funkcję która przyjmuje dwa argumenty: prefix: str, amount:int
#Wykorzystując wyrażenie genrujące przygotuj generator, który będzie zwracał wartości postaci prefix_XXX, gdzie XXX to liczba od 1 do amount,
# a liczba ta wypełniona jest zerami, np. dla inicjalnej wartości amount = 100, i aktualnej wartości amount=3 mamy prefix_003

def zadanie_7(prefix:str, amount:int):
    for i in range(1, amount + 1):
        yield f"{prefix}_{str(i).zfill(len(str(amount)))}"


for value in zadanie_7('test', 5):
    print(value)


# jeszcze do poprawy:
def zadanie_8(tekst):
    new_l = []
    for el in tekst:
        if el in string.digits:
            el = int(el)
            new_l.append(el)
    return new_l
    pass

# print(zadanie_8('1564asdad456444asd56446'))
# def main():
#     # zadanie_1()
# #    zadanie_2():
# #    zadanie_3():
# #    zadanie_4():
# #    zadanie_5():
# #    zadanie_6():
# #    zadanie_7():
# #    zadanie_8():
#
#
# if __name__ = '__main__':
#     main()
