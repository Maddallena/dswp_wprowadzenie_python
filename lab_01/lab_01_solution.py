#========== zad 2 =====================
# number = int(1)
# print(number)
# print(type(number))
#
# print(type(int(1)))
# #print(type(int("1")))
# print(int("110", base=16))
# #print(type(int("100", base=2)))
#
# print(int("1000", base=9))

number_int_1 = int("3", base=16)
number_int_2 = int("110", base=2)
print(number_int_1)
print(number_int_2)
print(int("1000", base=9))

number_float_1 = float("3")
number_float_2 = float("110")
number_float_3 = float(97 + 4)
number_float_4 = float(29//4)
print(number_float_1)
print(number_float_2)
print(number_float_3)
print(number_float_4)

#========== zad 3 =====================

# i = 100
# print(i.bit_count())

def population_count(number):
    return number.bit_count()

population_count(29)

def check_float(number):
    return number.is_integer()

check_float(29.05)

#========== zad 4 =====================

def alternatywa(x, y):
    return x ^ y

def koniunkcja(x, y):
    return x & y

def prawe_przesuniecie(x, n):
    return x >> n

def lewe_przesuniecie(x, n):
    return x << n

print(alternatywa(9, 10))
print(koniunkcja(9, 10))
print(prawe_przesuniecie(9, 2))
print(lewe_przesuniecie(9, 2))
