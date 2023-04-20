# ========================== Zadanie 1 ==========================
print('Zadanie 1\n')


# ========================== Zadanie 2 ==========================
print('\nZadanie 2\n')

# def zadanie2(lista_plikow, nowy_plik):
#     with open(f'{nowy_plik}','w') as plik:
#         for stary_plik in lista_plikow:
#             with open(stary_plik) as old_file:
#                 for line in old_file:
#                     plik.write(line)
#                 plik.write('\n')
#     return nowy_plik
#
# zadanie2(['cos1.txt', 'cos2.csv'], 'ostateczny_plik_3.txt')

# ========================== Zadanie 3 ==========================
print('\nZadanie 3\n')


# def values(n_najmniejszych, n_najwiekszych, lista_numeryczna):
#     not_number = False
#     nowa_lista = []
#     for el in lista_numeryczna:
#         if type(el) is not int and type(el) is not float:
#             # not_number = True
#             continue
#         else:
#             nowa_lista.append(el)
#
#     # if not_number:
#     #     print('Lista nie zawiera samych liczb.')
#     # else:
#     #     print('Lista ma w sobie tylko typ liczbowy.')
#
#     lista_najmniejszych = sorted(nowa_lista)[:n_najmniejszych]
#     lista_najwiekszych = sorted(nowa_lista)[:-n_najwiekszych-1:-1]
#     if nowa_lista:
#         if n_najmniejszych == 0:
#             print('lista_najwiekszych liczb: ')
#             return lista_najwiekszych
#         elif n_najwiekszych == 0:
#             print('lista_najmniejszych liczb: ')
#             return lista_najmniejszych
#         else:
#             return 'lista najmniejszych: ', lista_najmniejszych, 'lista najwiekszych: ', lista_najwiekszych
#     else:
#         return print('Lista nie zawiera w sobie typu liczbowego.')
#
# l = [5,2,7,'s',6,5,8,4,10,'p']
#
# print('proba 1')
# a = values(5,5,l)
# print(a)
#
# print('\nproba 2\n')
# b = values(5,0,l)
# print(b)
#
# print('\nproba 3\n')
# c = values(0,5,l)
# print(c)
# print()
# m = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# d = values(0,5,m)

# ========================== Zadanie 4 ==========================
print('\nZadanie 4\n')
# mieszana = [1, 2.3, 'Zbyszek', 5, 'Marian', 3.0]
#
# def slownik_wartosci(lista):
#     slownik = {}
#
#     for el in lista:
#         key = type(el).__name__
#         if key not in slownik:
#             slownik[key] = []
#             slownik[key].append(el)
#         else:
#             slownik[key].append(el)
#
#     return slownik
#
#
# print(slownik_wartosci(mieszana))

# ========================== Zadanie 5 ==========================
print('\nZadanie 5\n')

# 'A-M_nazwiska.txt' oraz 'N-Ż_nazwiska.txt'
from unidecode import unidecode
# import locale
#
# locale.setlocale(locale.LC_COLLATE, "pl_PL.UTF-8")
# words = 'Ala ala zen Ąęś coś bąk ćma bar COS'.split()
#
# words.sort(key=locale.strxfrm)
# print(' '.join(words))
# # def zadanie5(lista_nazwisk):
# #
# #     for el in range(len(lista_nazwisk)):
# #         lista_nazwisk[el] = unidecode(lista_nazwisk[el])
# #     with open('A-M_nazwiska.txt') as f1, open('N-Ż_nazwiska.txt') as f2:
# #         # 65-77
# #         # 78-90
# #     return lista_nazwisk
#
# nazwiska = ['Żmija', 'Ćwierk', 'Głogowska']
# nazwiska.sort(key=locale.strxfrm)
# print(' '.join(nazwiska))
# print(nazwiska[1][0])
# print(zadanie5(nazwiska))
# print(unidecode('kožušček'))
# ========================== Zadanie 6 ==========================
print('\nZadanie 6\n')
# def odwrocona_kolejnosc(zdanie):
#     # nowa_l = []
#     # for word in zdanie.split():
#     #   odwrotne = ''
#     #   for l in range(1,len(word)+1):
#     #       odwrotne += word[-l]
#     #   nowa_l.append(odwrotne)
#     # return ' '.join(nowa_l)
#
#     nowa_l = ' '.join([''.join([word[-l] for l in range(1, len(word) + 1)]) for word in zdanie.split()])
#     return nowa_l
#
# print(odwrocona_kolejnosc('Ala ma kota'))

# ========================== Zadanie 7 ==========================
print('\nZadanie 7\n')

import random

# def losowanie_kart():
#     kolory = ['pik', 'kier', 'trefl', 'karo']
#     figury = ['as', 'król', 'dama', 'walet', 10, 9, 8, 7, 6, 5, 4, 3, 2]
#     karty = []
#     while len(karty) < 20:
#
#         karta = ' '.join(map(str, [random.choice(figury), random.choice(kolory)]))
#
#         if karta not in karty:
#             karty.append(karta)
#     gracze = [karty[x:x + 5] for x in range(0, len(karty), 5)]
#     print(f'Karty graczy: \ngracz1 {gracze[0]}\ngracz2 {gracze[1]}\ngracz3 {gracze[2]}\ngracz4 {gracze[3]}')
#     return gracze
#
#
# losowanie_kart()

# ========================== Zadanie 8 ==========================
print('\nZadanie 8\n')



# def name_to_mail(plik_nazwisk, domena):
#
#     with open('mail_nazwiska.txt', 'w', encoding='utf-8') as plik1:
#         with open(f'{plik_nazwisk}', encoding='utf-8') as plik2:
#             for line in plik2:
#                 do_maila = unidecode(line.rstrip().lower()).split()
#                 mail =f'{".".join(do_maila)}@{domena}'
#                 plik1.write(line.rstrip() + ', ' + mail + '\n')
#
#     return plik1
#
#
# name_to_mail('nazwiska_z8.txt', 'student.uwm.edu.pl')

# ========================== Zadanie 9 ==========================
print('\nZadanie 9\n')


def kolo_fortuny(plik_hasla):
    gra = True
    with open(f'{plik_hasla}', 'r', encoding='utf-8') as plik:
        hasla = [line.rstrip() for line in plik]

    haslo = random.choice(hasla).split()
    # print(haslo)
    ukryte = [(['_' for l in haslo[x]]) for x in range(len(haslo))]

    while gra:

        odkryte = ''
        for el in ukryte:
            odkryte += ''.join(el)
            odkryte += ' '
        print()
        print(odkryte)
        print()

        zrobione = 0

        for i in range(len(ukryte)):
            if '_' not in ukryte[i]:
                zrobione += 1

        if zrobione < len(ukryte):
            odpowiedz = input('podaj litere/ literki lub cale haslo: ').lower().split()

            for el in range(len(odpowiedz)):
                for l in range(len(odpowiedz[el])):
                    litera_odg = odpowiedz[el][l]
                    for h in range(len(haslo)):
                        for c in range(len(haslo[h])):
                            if litera_odg == haslo[h][c]:
                                ukryte[h][c] = litera_odg

        else:
            print('gratulacje!')
            gra = False


kolo_fortuny('hasla.txt')
