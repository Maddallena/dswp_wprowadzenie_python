# ================================ zadanie 1 ======================================
import re
linia_danych = input("wprowadź linię danych z własnym separatorem: ")
separator_zrodlowy = input("wprowadz separator uzyty w zdaniu: ")
separator_docelowy = input("wprowadz separator docelowy: ")

lista_wyrazow = linia_danych.split(separator_zrodlowy)
print(lista_wyrazow)
nowe_zdanie = separator_docelowy.join(lista_wyrazow)
print(nowe_zdanie)

result = re.sub(separator_zrodlowy, separator_docelowy, linia_danych)
print(result)
# # https://docs.python.org/3/library/re.html

# ================================ zadanie 2 i 3 ======================================

lorem_ipsum = "Czym jest Lorem Ipsum? Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle " \
              "poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem " \
              "próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie " \
              "niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających " \
              "fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym " \
              "do realizacji druków na komputerach osobistych, jak Aldus PageMaker"

imie = "Magdalena"
nazwisko = "Rajewska"
litera_1 = imie[2]
litera_2 = nazwisko[3]
liczba_liter1 = lorem_ipsum.count(litera_1)
liczba_liter2 = lorem_ipsum.count(litera_2)
print(f"W tekście jest {liczba_liter1} liter {litera_1} oraz {liczba_liter2} liter {litera_2}")

