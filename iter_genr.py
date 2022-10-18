depth = 1
most_depth = 0
flat_list = []


def flat_generator(some_list):
    '''
    Функция-генератор плоского списка из двухмерного

    :return: None
    '''
    i = 0
    j = 0
    while True:
        try:
            current_item = some_list[j][i]
        except IndexError:
            i = 0
            j += 1
            try:
                current_item = some_list[j][i]
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
    global depth # переменная для хранения текущей глубины вложенности списка
    global most_depth # переменная для хранания наибольшей глубины вложенности
    global flat_list # переменная для хранения результатного плоского списка

    for element in deep_list:
        if type(element) == list:
            depth += 1
            unpack_unlim_list(element)
            continue
        else:
            flat_list.append(element)
            if depth > most_depth:
                most_depth = depth
            continue
    depth -= 1
    return (most_depth, flat_list)


def unpack_list_with_yield(some_deep_list):
    '''
    Функция-генератор списка
    :return: None
    '''
    depth, middle_list = unpack_unlim_list(some_deep_list)
    print('Глубина исходного списка: ', depth, 'уровней')
    print('Результатный плоский список:')
    for element in middle_list:
        yield element
    return


class FlatIterator():

    def __init__(self, some_list):
        self.main_list = some_list

    def __iter__(self):
        self.main_list_cursor = 0  # курсор основного списка
        self.nested_list_cursor = 0  # курсор вложенного списка
        return self

    def __next__(self):
        try:
            caught_element= self.main_list[self.main_list_cursor][
                self.nested_list_cursor]
            self.nested_list_cursor += 1
        except IndexError:
            self.nested_list_cursor = 0
            self.main_list_cursor += 1
            try:
                caught_element = self.main_list[self.main_list_cursor][
                    self.nested_list_cursor]
            except IndexError:
                raise StopIteration

        return caught_element
