# Домашнее задание «Итераторы, генераторы»

import time
import simple_colors
from iter_genr import FirstHwPoint, flat_generator, unpack_list_with_yield,\
    nested_list, deep_nested_list

if __name__ == '__main__':

    print()
    print(simple_colors.black('Исходный список:', ['bold']))
    print(nested_list)
    print()
    time.sleep(2)

    s = 'Реализация задания №1: Итератор'
    print(simple_colors.black(s, ['bold']))
    print('-' * len(s))
    print('Результатный плоский список:')
    my_list = FirstHwPoint()
    for item in my_list:
        print(item.common_list, end=' ')
    print()
    print()
    time.sleep(2)

    print('Результат list comprehension:')
    my_list_2 = FirstHwPoint()
    flat_list = [item.common_list for item in my_list_2]
    print(flat_list)
    print()
    time.sleep(2)

    s = 'Реализация задания №2: Генератор'
    print(simple_colors.black(s, ['bold']))
    print('-' * len(s))
    print('Результатный плоский список:')
    for item in flat_generator():
        print(item, end=' ')
    print()
    print()
    time.sleep(2)

    s = 'Реализация задания №4: Генератор для списка неограниченной ' \
        'вложенности'
    print(simple_colors.black(s, ['bold']))
    print('-'*len(s))
    print('С использованием yield:')
    print('Исходный "неограниченный" список:')
    print(deep_nested_list)
    for item in unpack_list_with_yield():
        print(item, end=' ')
    print()
    print()
