import copy
import string
# ================================= zad 1 =====================================
lista_zad1 = []

for x in range(1,11):
    lista_zad1.append(x)

print(f'Lista do zadania 1 i 2: {lista_zad1}')


nowa_lista_zad1 = lista_zad1[5:]
lista_zad1 = lista_zad1[:5]

print(f'Lista 1.1 po podziale: {lista_zad1}')
print(f'Lista 1.2 po podziale: {nowa_lista_zad1}')
print()
# ================================= zad 2 =====================================

lista_zad2 = lista_zad1 + nowa_lista_zad1
print(f'Lista 2.0 po połączeniu list z zad1: {lista_zad2}')
lista_zad3 = copy.deepcopy(lista_zad2)
lista_zad3.insert(0,0)
print(f'Lista 2.1 po dodaniu 0 na indeksie 0: {lista_zad3}')
print()
# ================================= zad 3 =====================================
print("Zadanie 3:\n")
def skryp_zad3():
    tekst = input("Wprowadź dowolny tekst: ")
    nowy_tekst = ''.join(sorted(set(tekst.lower()))).strip()
    return nowy_tekst

zad3 = skryp_zad3()
print(f'Zbiór znaków uporządkowany alfabetycznie: {zad3}')
print()
# ================================= zad 4 =====================================

pl_miesiace = {1: 'Styczeń',
      2: 'Luty',
      3: 'Marzec',
      4: 'Kwiecień',
      5: 'Maj',
      6: 'Czerwiec',
      7: 'Lipiec',
      8: 'Sierpień',
      9: 'Wrzesień',
      10: 'Październik',
      11: 'Listopad',
      12: 'Grudzień'}

# ================================= zad 5 =====================================

en_months = {1: 'January',
      2: 'February',
      3: 'March',
      4: 'April',
      5: 'May',
      6: 'June',
      7: 'July',
      8: 'August',
      9: 'September',
      10: 'October',
      11: 'November',
      12: 'Dicember'}


months = {'pl': pl_miesiace,
          'en': en_months}

print(f"Zadanie 4 i 5:\nmonths['pl'][4]= {months['pl'][4]}'\nmonths['en'][4] = {months['en'][4]}")
print()
# ================================= zad 6 =====================================

str = 'Marianna'
l = []
for char in str:
    if char in l:
        continue
    l.append(char)

new_dict = dict.fromkeys(l,1)

new_dict_1 = dict.fromkeys(str,1)

print(f'Zadanie 6: \nmetoda 1: {new_dict} \nmetoda 2: {new_dict_1}')
print()
# ================================= zad 7 =====================================

zad_7 = input('Wprowadź dowolny łańcuch znaków: ').lower()

ascii_lower = 0
str_digits = 0

for el in zad_7:
    if el in string.ascii_lowercase:
        ascii_lower += 1
    if el in string.digits:
        str_digits += 1
print('\nMetoda 1: \n')
print(f'W Twoim łańcuchu znaków "{zad_7}" jest: \n'
      f'{ascii_lower:>3} znaków pokrywających się z string.ascii_lowercase, co stanowi {(ascii_lower * 100)/len(zad_7):.2f}% całego łańcucha oraz \n'
      f'{str_digits:>3} znaków pokrywających się z string.digits, co stanowi {(str_digits * 100)/len(zad_7):.2f}% całego łańcucha')

print('\nMetoda 2: \n')
chars = sum((ch in string.ascii_lowercase) for ch in zad_7)
digits = sum((dg in string.digits) for dg in zad_7)
# print(chars)
# print(digits)

p_chars = (chars * 100)/len(zad_7)
p_digits = (digits * 100)/len(zad_7)

print(f'W Twoim łańcuchu znaków "{zad_7}" jest: \n'
      f'{chars:>3} znaków pokrywających się z string.ascii_lowercase, co stanowi {p_chars:.2f}% całego łańcucha oraz \n'
      f'{digits:>3} znaków pokrywających się z string.digits, co stanowi {p_digits:.2f}% całego łańcucha')

# sd;vjlvdf16484

