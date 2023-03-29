# ========================== Zadanie 1 ==========================
print("Zadanie 1\n")

number = int(input("Wprowadź liczbę całkowitą: "))
print(f"Postać binarna: {bin(number)}")
print(f"Postać ósemkowa: {oct(number)}")
print(f"Postać szesnastkowa: {hex(number)}")

# ========================== Zadanie 2 ==========================
print("\nZadanie 2\n")

def zad2():
    i = input("Wprowadź wartość: ")

    try:
        int_i_v = int(i)
        print(f"Wartość {i} jest rzutowalna na typ int")
    except ValueError:
        print(f"Wartość {i} nie jest rzutowalna na typ int")
    try:
        float_i_v = float(i)
        print(f"Wartość {i} jest rzutowalna na typ float")
    except ValueError:
        print(f"Wartość {i} nie jest rzutowalna na typ float")


zad2()
# ========================== Zadanie 3 ==========================
print("\nZadanie 3\n")
import sys
def zapis():
    s = sys.stdin.readline()
    liczba = s[:-1]
    dec = [10**i for i in range(len(liczba))]
    sys.stdout.write("Podaną liczbę można zapisać jako: ")

    for el in range(len(liczba)):
        sys.stdout.write(str(dec[-(el+1)]) + " * " + str(liczba[el]))
        if el != len(liczba)-1:
            sys.stdout.write(" + ")

zapis()
# ========================== Zadanie 4 ==========================
print("\nZadanie 4\n")
import this

def skrypt():

    zdanie = input("\nWprowadź zdanie: ")
    print(''.join(this.d.get(el, el) for el in zdanie))

skrypt()

# ========================== Zadanie 5 ==========================
print("\nZadanie 5\n")

def zadanie5():
    zdanie = input("Wpisz zdanie: ").split()
    return sorted(zdanie, key=len)

print(zadanie5())

# ========================== Zadanie 6 ==========================
print("\nZadanie 6\n")
import random
def zadanie6():
    tabela = [['Koleżanki i koledzy', 'Z drugiej strony', 'Podobnie', 'Nie zapominajmy jednak, że', 'W ten oto sposób',
               'Praktyka dnia codziennego dowodzi, że',
               'Wagi i znaczenia tych problemów nie trzeba szerzej uzasadniać, ponieważ',
               'Różnorakie i bogate doświadczenia', 'Troska organizacji, a szczególnie', 'Wyższe założenia ideowe, a także'],
              ['realizacja nakreślonych zadań programowych', 'zakres i miejsce szkolenia kadr',
               'stały wzrost ilości i zakres naszej aktywności', 'aktualna struktura organizacji',
               'nowy model działalności organizacyjnej', 'dalszy rozwój różnych form działalności',
               'stałe zabezpieczenie informacyjno programowe naszej działalności', 'wzmacnianie i rozwijanie struktur',
               'konsultacja z szerokim aktywem', 'rozpoczęcie powszechnej akcji kształtowania postaw'],
              ['zmusza nas do przeanalizowania', 'spełnia istotną rolę w kształtowaniu', 'wymaga sprecyzowania i określenia',
               'pomaga w przygotowaniu i realizacji', 'zabezpiecza udział szerokiej grupie w kształtowaniu',
               'spełnia ważne zadania w wypracowaniu', 'umożliwia w większym stopniu tworzenie', 'powoduje docenianie wagi',
               'przedstawia intersującą próbę sprawdzenia', 'pociąga za sobą proces wdrażania i unowocześniania'],
              ['istniejących warunków administracyjno- finansowych.', 'dalszych kierunków rozwoju.',
               'systemu powszechnego uczestnictwa.', 'postaw uczestników wobec zadań stawianych przez organizację.',
               'nowych propozycji.', 'kierunków postępowego wychowania.', 'systemu szkolenia kadry odpowiadającego potrzebom.',
               'odpowiednich waruknków aktywizacji.', 'modelu rozwoju.', 'form oddziaływania.']]

    ilosc_zdan = int(input('ile chcesz zdań?: '))
    wypowiedz = ""
    for i in range(ilosc_zdan):
        for j in range(len(tabela)):
            wypowiedz += tabela[j][random.randint(0,len(tabela[j])-1)]
            wypowiedz += " "
        wypowiedz += "\n"
    return wypowiedz

p = zadanie6()
print(p)


