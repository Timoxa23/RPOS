
# Выполнил: Тимофеев А.С.
# Группа: МС-32

def print_with_border(string, char):

    border_length = len(string) + 4
    print(char * border_length)
    print(f"{char} {string} {char}")
    print(char * border_length)

s = input("Введите строку: ")
k = input("Введите символ рамки: ")

print_with_border(s, k)

# --------------
# Пример вывода:
#
# Введите строку: Просто текст
# Введите символ: +
# ++++++++++++++
# +Просто текст+
# ++++++++++++++
