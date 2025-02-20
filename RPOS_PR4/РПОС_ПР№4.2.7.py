# Выполнил: Тимофеев А.С.
# Группа: МС-32

def has_digits(sentence):

    return any(char.isdigit() for char in sentence)

def sentences_with_digits_count(sentences):

    return sum(1 for sentence in sentences if has_digits(sentence))

n = int(input("Введите количество предложений: "))  # Запрашиваем количество предложений

sentences = []
for i in range(n):
    sentences.append(input(f"Введите предложение {i+1}: "))

count = sentences_with_digits_count(sentences)

print(f"Количество предложений, содержащих хотя бы одну цифру: {count}")

# --------------
# Пример вывода:
#
# Введите количество предложений: 3
# Введите предложение №1:
# Просто текст
# Введите предложение №2:
# Текст с цифрой 1 (один)
# Введите предложение №3:
# Тут нет цифры
# Предложений с цифрой = 1
