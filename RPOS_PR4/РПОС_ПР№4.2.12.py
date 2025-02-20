# Выполнил: Тимофеев А.С.
# Группа: МС-32

data = [
    {1: 'м', 2: 'м', 3: 'м', 4: 'ж'},
    {1: 'ж', 2: 'м', 3: 'ж', 4: 'ж'},
    {1: 'ж', 2: 'ж', 3: 'ж', 4: 'ж'},
    {1: 'м', 2: 'м', 3: 'м', 4: 'м'},
    {1: None, 2: None, 3: None, 4: None},
    {1: 'м', 2: None, 3: None, 4: 'ж'},
    {1: None, 2: None, 3: None, 4: None},
    {1: 'м', 2: 'м', 3: None, 4: 'м'},
    {1: 'ж', 2: None, 3: None, 4: 'ж'}
]

def vacant_compartments(data):

    return [i + 1 for i, compartment in enumerate(data) if all(v is None for v in compartment.values())]

def vacant_seats(data, compartments_condition=None, seat_condition=None):

    result = []
    for i, compartment in enumerate(data):
        if compartments_condition is None or compartments_condition(compartment):
            for seat, value in compartment.items():
                if seat_condition is None or seat_condition(seat, value):
                    if value is None:
                        result.append((i + 1, seat))
    return result

def is_same_sex_and_vacant(compartment, sex):

    non_vacant_seats = [v for v in compartment.values() if v is not None]
    return all(v == sex for v in non_vacant_seats) and any(v is None for v in compartment.values())

# список полностью свободных купе
print("Список полностью свободных купе:", vacant_compartments(data))
# список свободных мест в вагоне
print("Список свободных мест в вагоне:", vacant_seats(data))
# список свободных нижних мест
print("Список свободных нижних мест:", vacant_seats(data, seat_condition=lambda seat, value: seat % 2 != 0))
# список свободных верхних мест
print("Список свободных верхних мест:", vacant_seats(data, seat_condition=lambda seat, value: seat % 2 == 0))
# список свободных мест в купе с исключительно мужской компанией
print("Список свободных мест в купе с исключительно мужской компанией:", vacant_seats(data, compartments_condition=lambda x: is_same_sex_and_vacant(x, "м")))
# список свободных мест в купе с исключительно женской компанией
print("Список свободных мест в купе с исключительно женской компанией:", vacant_seats(data, compartments_condition=lambda x: is_same_sex_and_vacant(x, "ж")))

# --------------
# Пример вывода:
#
# [5, 7]
# [(5, 1), (5, 2), (5, 3), (5, 4), (6, 2), (6, 3), (7, 1), (7, 2), (7, 3),
#  (7, 4), (8, 3), (9, 2), (9, 3)]
# [(5, 1), (5, 3), (6, 3), (7, 1), (7, 3), (8, 3), (9, 3)]
# [(5, 2), (5, 4), (6, 2), (7, 2), (7, 4), (9, 2)]
# [(8, 3)]
# [(9, 2), (9, 3)]
