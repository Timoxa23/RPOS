# Выполнил: Тимофеев А.С.
# Группа: МС-32

def gcd(first, second):

    while second:
        first, second = second, first % second
    return first

def lcm(first, second):

    return first * second // gcd(first, second)

def gcd_nums(nums):

    from functools import reduce
    return reduce(gcd, nums)

def lcm_nums(nums):

    from functools import reduce
    return reduce(lcm, nums)


nums = list(map(int, input("Введите числа через пробел: ").split()))

print("НОД чисел из списка:", gcd_nums(nums))
print("НОК чисел из списка:", lcm_nums(nums))

# --------------
# Пример вывода:
#
# Введите числа через пробел: 8 10 14
# НОД = 2
# НОК = 280
#
# Введите числа через пробел: 6 8 24 16
# НОД = 2
# НОК = 48
