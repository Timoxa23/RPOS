def find_last_index(lst, element):
    try:
        return len(lst) - 1 - lst[::-1].index(element)
    except ValueError:
        return -1

# Проверяем на данных списках
num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']

# Примеры вызова функции
print(find_last_index(num_list, 10))   # Вывод: 4
print(find_last_index(word_list, 'ruby'))  # Вывод: 6
