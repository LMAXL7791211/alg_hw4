#  2. Написать два алгоритма нахождения i-го по счёту простого числа.
#
#     Без использования «Решета Эратосфена»;
#     Используя алгоритм «Решето Эратосфена»
#
#  Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
#  Результаты анализа сохранить в виде комментариев в файле с кодом.

import cProfile
import timeit

"""
# Вариант с использованием алгоритма «Решето Эратосфена»

def sieve(n):
    print(f'Ищем в диапазоне до {n}...')

    a = [k for k in range(n)]  # заполнение массива значениями от 0 до n-1

    # вторым элементом является единица, которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0

    m = 2  # замена на 0 начинается с 3-го элемента (первые два уже нули)
    while m < n:  # перебор всех элементов до заданного числа
        if a[m] != 0:  # если он не равен нулю, то
            j = m * 2  # увеличить в два раза (текущий элемент простое число)
            while j < n:
                a[j] = 0  # заменить на 0
                j = j + m  # перейти в позицию на m больше
        m += 1
    return a


def main():
    print('Алгоритм с использованием решета Эратосфена')
    i = int(input('Введите i (какое по номеру простое число вы хотите найти) -->'))
    # i = 5

    a_try = []
    num = 10  # начнем искать в диапазоне до 10

    while i >= (len(a_try)):
        a_try = list(set(sieve(num)))  # формирование массива простых и удаление нулей
        num *= 10  # будем увеличивать область поиска на порядок с каждой итерацией

    # вывод простых чисел на экран
    a_try.sort()
    #print(a_try)
    print(f'Всего найдено {len(a_try)-1} простых чисел')
    print(f'{i}-е простое число = {a_try[i]}')


main()
# cProfile.run('main()')
# print(timeit.timeit("main()", setup="from __main__ import main"))
"""

"""
Алгоритм с использованием решета Эратосфена

timeit:
i = 5 . Вывод (принты) в программе я закомментировал, запускал без них
timeit: 51.851495568



i = 10000
CProfile:
Всего найдено 78498 простых чисел
10000-е простое число = 104729
         34 function calls in 1.165 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.008    0.008    1.165    1.165 <string>:1(<module>)
        6    0.957    0.160    1.047    0.175 alg_hw4_2.py:15(sieve)
        6    0.090    0.015    0.090    0.015 alg_hw4_2.py:18(<listcomp>)
        1    0.090    0.090    1.156    1.156 alg_hw4_2.py:34(main)
        1    0.000    0.000    1.165    1.165 {built-in method builtins.exec}
        8    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        9    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.020    0.020    0.020    0.020 {method 'sort' of 'list' objects}

"""

# Вариант без использования алгоритма «Решето Эратосфена»


def is_prime(n):
    for j in range(3, int(n ** 0.5) + 1):
        if n % j == 0:
            return False
    return True


def search(n):
    primes = [2]
    i = 3
    while len(primes) < n:
        if is_prime(i) == 1:
            primes.append(i)
        i += 2
    return primes


def main():
    print('Алгоритм без использования решета Эратосфена')
    num = int(input('Введите i (какое по номеру простое число вы хотите найти) -->'))
    # num = 5
    a_try = search(num)
    prime_num = a_try[num - 1]
    # print(a_try)
    print(f'Всего найдено {len(a_try)} простых чисел')
    print(f'{num}-е простое число = {prime_num]}')


main()
#  cProfile.run('main()')
#  print(timeit.timeit("main()", setup="from __main__ import main"))

"""
Алгоритм без использования решета Эратосфена

timeit:
i = 5 . Вывод (принты) в программе я закомментировал, запускал без них

7.742026932000001


num = 10000
cProfile:

Всего найдено 10000 простых чисел
10000-е простое число = 104729
         114737 function calls in 0.447 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.447    0.447 <string>:1(<module>)
        1    0.031    0.031    0.447    0.447 alg_hw4_2.py:103(search)
        1    0.000    0.000    0.447    0.447 alg_hw4_2.py:113(main)
    52364    0.409    0.000    0.409    0.000 alg_hw4_2.py:96(is_prime)
        1    0.000    0.000    0.447    0.447 {built-in method builtins.exec}
    52366    0.006    0.000    0.006    0.000 {built-in method builtins.len}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.print}
     9999    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""