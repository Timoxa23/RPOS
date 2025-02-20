# Выполнил: Тимофеев А.С.
# Группа: МС-32

def sentence_stats(sentence):

    sentence = sentence.lower()
    stats = {}
    for char in sentence:
        if char in stats:
            stats[char] += 1
        else:
            stats[char] = 1
    return stats

s = input("Введите предложение: ")

statistics = sentence_stats(s)

for char, count in statistics.items():
    print(f"{char} = {count}")

# --------------
# Пример вывода:
#
# Введите предложение: мама МЫла РамУ
# {'л': 1, 'р': 1, 'у': 1, 'м': 4, 'а': 4, 'ы': 1, ' ': 2}
