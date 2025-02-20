# Выполнил: Тимофеев А.С.
# Группа: МС-32

LETTERS_EX = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
DIGITS_EX = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

def to_base(number, base):

    if number == 0:
        return "0"
    result = ""
    while number > 0:
        remainder = number % base
        if remainder >= 10:
            result = LETTERS_EX[remainder] + result
        else:
            result = str(remainder) + result
        number //= base
    return result

def from_base(number, base):

    result = 0
    power = 0
    for digit in reversed(number):
        if digit in DIGITS_EX:
            result += DIGITS_EX[digit] * (base ** power)
        else:
            result += int(digit) * (base ** power)
        power += 1
    return result


decimal_number = int(input("Введите десятичное число: "))
base = int(input("Введите систему счисления для перевода (от 2 до 16): "))

converted_number = to_base(decimal_number, base)
print(f"{decimal_number} в системе счисления {base} равно {converted_number}")


number_in_base = input(f"Введите число в системе счисления {base}: ")
decimal_result = from_base(number_in_base, base)
print(f"{number_in_base} в десятичной системе равно {decimal_result}")

# --------------
# Пример вывода:
#
# Нет
