#================================= Zadanie 1 ============================================
print('Zadanie 1')
# Wykorzystując przykład z listingu 2 napisz kod,
# który przetestuje czas inicjowania tablicy znaków oraz wartości całkowitych (typ int i long)
# i porówna z czasem zainicjowania listy z takimi samymi wartościami.


# test czasu wykonania
from timeit import timeit
import random
# setup = """
# from array import array
# import random
# """
# stmt1 = """
# tab_of_floats = array('f', [random.random() for _ in range(1_000_000)])
# """
# stmt2 = """
# list_of_floats = [random.random() for _ in range(1_000_000)]
# """
#
# # print(timeit(stmt1, setup, number=100))
# # print(timeit(stmt2, setup, number=100))
#
# stmt3 = """
# tab_of_integers = array('I', [random.randint(1,10) for _ in range(1_000_000)])
# """
# stmt4 = """
# list_of_integers: list[int] = [random.randint(1,10) for _ in range(1_000_000)]
# """
# stmt5 = """
# tab_of_integers = array('L', [random.randint(1000000000,2000000000) for _ in range(1_000_000)])
# """
# stmt6 = """
# list_of_integers: list[int] = [random.randint(1000000000,2000000000) for _ in range(1_000_000)]
# """
#
# print(timeit(stmt3, setup, number=100))  # 95.7791894999973
# print(timeit(stmt4, setup, number=100))  # 90.2173507999978
# print()
#
# print(timeit(stmt5, setup, number=100))  # 95.7791894999973
# print(timeit(stmt6, setup, number=100))  # 90.2173507999978
# print()
#================================= Zadanie 2 ============================================
print('Zadanie 2')

from array import array

# zapisanie tablicy do pliku oraz jej wczytanie
tab_of_floats = array('f', [random.random() for _ in range(1_000_000)])

with open('floats_array.bin', 'wb') as file_arr:
    tab_of_floats.tofile(file_arr)

# wczytujemy ponownie dane do tablicy floatów
tab_of_floats_loaded = array('f')
file_arr  = open('floats_array.bin', 'rb')
tab_of_floats_loaded.fromfile(file_arr, 1_000_000)
file_arr.close()


# i analogiczna operacja dla listy
list_of_floats = [random.random() for _ in range(1_000_000)]
with open('floats_list.txt', 'w') as file_arr:
    file_arr.writelines('\n'.join([str(x) for x in list_of_floats]))

with open('floats_list.txt', 'r') as file_list:
    list_of_floats_loaded = file_list.readlines()

list_of_floats_loaded = [float(x.strip()) for x in list_of_floats_loaded]
print(list_of_floats_loaded[:10])

setup = """
from array import array
tab_of_floats = array('f', [random.random() for _ in range(1_000_000)])
"""
#================================= Zadanie 3 ============================================
# print('Zadanie 3')


#================================= Zadanie 4 ============================================
# print('Zadanie 4')


#================================= Zadanie 5 ============================================
# print('Zadanie 5')




#================================= Zadanie 6 ============================================
# print('Zadanie 6')



#================================= Zadanie 7 ============================================
# print('Zadanie 7')