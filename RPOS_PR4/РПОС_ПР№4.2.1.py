#
# Выполнил: Тимофеев А.С
# Группа: МС-32
#

def sgn(x):

    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

x = float(input("Введите x: "))
y = float(input("Введите y: "))

z = (sgn(x) + y ** 2) / (sgn(y) - abs(x) ** 0.5)

print("Ответ:", round(z, 2))

# --------------
# Пример вывода:
#
# Введите x: -9
# Введите y: 0
# Ответ: 0.33