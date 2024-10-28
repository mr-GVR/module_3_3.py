def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# Вызов функции с разным количеством аргументов
print_params()  # Ожидаемый вывод: 1 строка True
print_params(10)  # Ожидаемый вывод: 10 строка True
print_params(b=25)  # Ожидаемый вывод: 1 25 True
print_params(c=[1, 2, 3])  # Ожидаемый вывод: 1 строка [1, 2, 3]

values_list = [42, 'пример строки', False]
values_dict = {'a': 100, 'b': 'текст', 'c': [7, 8, 9]}

# Вызов функции с распаковкой
print_params(*values_list)  # Ожидаемый вывод: 42 пример строки False
print_params(**values_dict)  # Ожидаемый вывод: 100 текст [7, 8, 9]

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)  # Ожидаемый вывод: 54.32 Строка 42