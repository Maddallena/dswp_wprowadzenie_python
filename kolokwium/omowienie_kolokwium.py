def zadanie_1(tekst: str):
    klucze = 'lower upper digits'.split(' ')
    slownik = dict.fromkeys(klucze, 0)

    for znak in tekst:
        if znak.isdigit():
            slownik['digits'] += 1
        elif znak.isupper():
            slownik['upper'] += 1
        elif znak.islower():
            slownik['lower'] += 1
    return slownik


def zadanie_2(n: int):
    tekst = input('wpisz tekst\n')
    # print(f'{tekst} ' * n, end = '')
    # print(*'A' * 5)
    # return tekst * n
    return f'{tekst} ' * n


def zadanie_3():
    import random
    wyrazy = input('wpisz co najmniej 3 wyrazy').split(' ')
    random.shuffle(wyrazy)
    return ' '.join(wyrazy[:3]).capitalize()


def zadanie_5(liczby: list[int], m):

    max_pozycje = len(str(max(liczby)))

    return [f'{x:0{max_pozycje}}' for x in liczby]

def zadanie_6(tekst: str, max_dlugosc: int):
    wyrazy = tekst.split(' ')
    output = ''
    for wyraz in wyrazy:
        if len(output + wyraz) > max_dlugosc:
            return output
        else:
            output += wyraz


def zadanie_7(prefix, amount):
    gen = (f'{prefix}_{x:>4}' for x in range(amount))


gen = zadanie_7('book', 100)
print(next(gen))
print(next(gen))
print(next(gen))
print(list(gen)) # zapisuje wszystkie do listy



