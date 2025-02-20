# Выполнил: Тимофеев А.С.
# Группа: МС-32

def avg(data):

    return sum(data) / len(data)

def cleared_data(data):

    return [x for x in data if x is not None]

n = int(input("Кол-во измерений: "))

data = []
for i in range(n):
    value = input(f"Измерение {i+1}-е: ")
    if value == '-':
        data.append(None)
    else:
        data.append(int(value))

clean_data = cleared_data(data)

average_temperature = avg(clean_data)

print(f"Средняя температура: {average_temperature:.2f}")


# --------------
# Пример вывода:
#
# Кол-во измерений: 3
# Измерение 1-е: 10
# Измерение 2-е: -
# Измерение 3-е: 20
# Средняя температура: 15.00
