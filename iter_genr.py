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
         ['c71']
         ], 'c52'], 'c42']]],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

depth = 1
fl = 0
help_list = []
flat_list = []


def flat_generator():
    '''
    Функция-генератор плоского списка из двухмерного

    :return: None
    '''
    i = 0
    j = 0
    while True:
        try:
            current_item = nested_list[j][i]
        except IndexError:
            i = 0
            j += 1
            try:
                current_item = nested_list[j][i]
            except IndexError:
                break
        yield current_item
        i += 1


def unpack_unlim_list(deep_list: list):
    '''
    Рекурсивная функция формирования плоского списка из многомерного.

    :param deep_list: Входной n-мерный список. С каждым рекурсивным
    вызовом n уменьшается пока не станет =1
    :return: количество уровней исходного списка и результатный плоский список
    '''
    global depth
    global fl
    global help_list
    global flat_list

    for element in deep_list:
        if type(element) == list:
            depth += 1
            fl += 1
            unpack_unlim_list(element)
            continue
        else:
            flat_list.append(element)
            if fl > 0:
                fl = 0
                help_list.append(depth)

            continue
    depth -= 1
    return (max(help_list), flat_list)


def unpack_list_with_yield():
    '''
    Функция-генератор списка
    :return: None
    '''
    depth, middle_list = unpack_unlim_list(deep_nested_list)
    print('Глубина исходного списка: ', depth, 'уровней')
    print('Результатный плоский список:')
    for element in middle_list:
        yield element
    return


class FirstHwPoint():

    def __init__(self):
        self.list_index = 0
        self.element_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.common_list = nested_list[self.list_index][
                self.element_index]
        except IndexError:
            self.element_index = 0
            self.list_index += 1
            try:
                self.common_list = nested_list[self.list_index][
                    self.element_index]
            except IndexError:
                raise StopIteration
        self.element_index += 1
        return self
