
class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.outer_index = 0  # Индекс для внешнего списка
        self.inner_index = 0  # Индекс для внутреннего списка

    def __iter__(self):
        return self

    def __next__(self):
        # Проверяем, есть ли еще элементы во вложенных списках
        while self.outer_index < len(self.list_of_list):
            # Получаем текущий внутренний список
            inner_list = self.list_of_list[self.outer_index]

            # Проверяем, есть ли еще элементы в текущем внутреннем списке
            if self.inner_index < len(inner_list):
                item = inner_list[self.inner_index]
                self.inner_index += 1  # Переходим к следующему элементу
                return item
            else:
                # Если внутренний список закончился, переходим к следующему внешнему списку
                self.outer_index += 1
                self.inner_index = 0  # Сброс индекса внутреннего списка

        # Если внешние списки тоже закончились, вызываем StopIteration
        raise StopIteration


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    # Проверка теста о корректности
    try:
        test_1()
        print("Тест пройден успешно!")
    except AssertionError:
        print("Тест не пройден. Проверьте реализацию FlatIterator.")

    # Вывод плоского представления
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    flat_iterator = FlatIterator(list_of_lists_1)
    flattened_list = list(flat_iterator)
    print("Плоское представление:", flattened_list)