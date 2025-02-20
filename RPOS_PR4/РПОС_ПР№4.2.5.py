# Выполнил: Тимофеев А.С.
# Группа: МС-32

def is_leap(year):

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days(month, year):

    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap(year) else 28


def another_date(day, month, year, delta=1):

    def previous_date(day, month, year):

        if day > 1:
            return day - 1, month, year
        elif month == 1:
            return 31, 12, year - 1
        else:
            prev_month = month - 1
            prev_day = days(prev_month, year)
            return prev_day, prev_month, year

    def next_date(day, month, year):

        if day < days(month, year):
            return day + 1, month, year
        elif month == 12:
            return 1, 1, year + 1
        else:
            return 1, month + 1, year

    while delta != 0:
        if delta > 0:
            day, month, year = next_date(day, month, year)
            delta -= 1
        elif delta < 0:
            day, month, year = previous_date(day, month, year)
            delta += 1

    return day, month, year

day, month, year = map(int, input("Введите день, месяц и год через пробел: ").split())
delta = int(input("Введите количество дней для добавления/вычитания (с положительным или отрицательным значением): "))


new_day, new_month, new_year = another_date(day, month, year, delta)


print(f"Новая дата: {new_day:02}.{new_month:02}.{new_year}")

# --------------
# Пример вывода:
#
# День, месяц, год через пробел: 1 1 2000
# Свдиг (может быть отрицательным): -2
# Новый день: 30/12/1999
#
# День, месяц, год через пробел: 1 1 2000
# Свдиг (может быть отрицательным): 2
# Новый день: 03/01/2000
