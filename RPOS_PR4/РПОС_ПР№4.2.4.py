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

day, month, year = map(int, input("Введите день, месяц и год через пробел: ").split())

prev_day, prev_month, prev_year = previous_date(day, month, year)
next_day, next_month, next_year = next_date(day, month, year)


print(f"Вчерашняя дата: {prev_day:02}.{prev_month:02}.{prev_year}")
print(f"Завтрашняя дата: {next_day:02}.{next_month:02}.{next_year}")

# --------------
# Пример вывода:
#
# День, месяц, год через пробел: 1 3 2000
# Предыдущий день: 29/02/2000
# Следующий день: 02/03/2000
