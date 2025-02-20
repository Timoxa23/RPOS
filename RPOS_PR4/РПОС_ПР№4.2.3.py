# Выполнил: Тимофеев А.С.
# Группа: МС-32

def is_lucky(num):

    even_count = 0
    odd_count = 0
    for digit in str(num):
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count == odd_count

def lucky_numbers(a, b):

    lucky_tickets = []
    for num in range(a, b + 1):
        if is_lucky(num):
            lucky_tickets.append(num)
    return lucky_tickets

a = int(input("Первый номер билета: "))
b = int(input("Последний номер билета: "))

lucky_tickets = lucky_numbers(a, b)


print(" ".join(map(str, lucky_tickets)))

# --------------
# Пример вывода:
#
# Первый номер билета: 10
# Последний номер билета: 25
# 10 12 14 16 18 21 23 25
