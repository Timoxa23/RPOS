# Выполнил: Тимофеев А.С.
# Группа: МС-32

def ceasar(text, shift):

    letters = [chr(i) for i in range(ord('а'), ord('я') + 1)]
    result = []
    for char in text:
        if char.lower() in letters:
            is_upper = char.isupper()
            index = letters.index(char.lower())
            new_index = (index + shift) % len(letters)
            new_char = letters[new_index]
            if is_upper:
                new_char = new_char.upper()
            result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)


text = input("Введите строку: ")
shift = int(input("Введите сдвиг: "))

encoded = ceasar(text, shift)

decoded = ceasar(encoded, -shift)

print("Зашифрованная строка:", encoded)
print("Расшифрованная строка:", decoded)

# --------------
# Пример вывода:
#
# Введите предложение: ПрограММиРОВание С++
# Введите сдвиг: 4
# Зашифрованная строка: УфтзфдРРмФТЖдсмй Х++
# Расшифрованная строка: ПрограММиРОВание С++
