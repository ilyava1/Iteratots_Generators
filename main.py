# Домашнее задание «Итераторы, генераторы»

import time
import simple_colors
from iter_genr import FlatIterator, flat_generator, unpack_list_with_yield

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

deep_nested_list = [
    [['a31', 'a32'], 'a', 'b', 'c',
     ['c31', 'c32',
      ['c41',
       ['c51',
        ['c61', 'c62',
         ['c71', ['c81']]
         ], 'c52'], 'c42']]],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

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
    flat_list = []
    for item in FlatIterator(nested_list):
        flat_list.append(item)
    print(flat_list)
    print()
    time.sleep(2)

    s = 'Реализация задания №2: Генератор'
    print(simple_colors.black(s, ['bold']))
    print('-' * len(s))
    print('Результатный плоский список:')
    for item in flat_generator(nested_list):
        print(item, end=' ')
    print()
    print()
    time.sleep(2)

    s = 'Реализация задания №4: Генератор для списка неограниченной ' \
        'вложенности'
    print(simple_colors.black(s, ['bold']))
    print('-'*len(s))
    print('Исходный "неограниченный" список:')
    print(deep_nested_list)
    print()
    for item in unpack_list_with_yield(deep_nested_list):
        print(item, end=' ')
    print()
    print()
