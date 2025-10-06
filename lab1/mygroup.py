"""Вывод списка студентов группы с информацией о результатах экзаменов

- print_students: Вывод списка студентов группы с информацией об экзаменах.
- filter_students_by_avg: Фильтрация студентов по среднему баллу.
"""

# Список студентов группы с информацией об экзаменах
groupmates = [
    {
        "name": "Максим",
        "surname": "Соловьев",
        "exams": ["ОС", "История", "УД"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Алексей",
        "surname": "Обласов",
        "exams": ["КТП", "История", "Физика"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Никита",
        "surname": "Шулапов",
        "exams": ["ОС", "АиГ", "ИС"],
        "marks": [5, 3, 4]
    },
    {
        "name": "Дмитрий",
        "surname": "Шагаров",
        "exams": ["История", "ОС", "КТП"],
        "marks": [3, 5, 5]
    },
    {
        "name": "Юрий",
        "surname": "Алексанов",
        "exams": ["ИС", "Электроника", "Философия"],
        "marks": [4, 3, 4]
    },
    {
        "name": "Никита",
        "surname": "Молоканов",
        "exams": ["КТП", "СиАОД", "АиГ"],
        "marks": [5, 3, 5]
    }
]


def print_students(students: list) -> None:
    """Вывод списка всех студентов с информацией об экзаменах.

    Использует .ljust для выравнивания строк таблицы, вывод в кодировке Unicode.

    Args:
        students (list): Список студентов группы для вывода.
    """
    print(
        u"Имя".ljust(20),
        u"Фамилия".ljust(20),
        u"Экзамены".ljust(50),
        u"Оценки".ljust(20),
        u"Средний балл".ljust(20),
    )
    for student in students:
        avg_mark = sum(student["marks"]) / len(student["marks"])
        print(
            student["name"].ljust(20),
            student["surname"].ljust(20),
            str(student["exams"]).ljust(50),
            str(student["marks"]).ljust(20),
            f"{avg_mark:.2f}".ljust(20),
        )


def filter_students_by_avg(students: list, min_avg: float) -> list:
    """Фильтрация студентов по среднему баллу.

    Args:
        students (list): Список студентов группы.
        min_avg (float): Минимальный средний балл для фильтрации.

    Returns:
        list: Список студентов, у которых средний балл >= min_avg.
    """
    return [
        student
        for student in students
        if sum(student["marks"]) / len(student["marks"]) >= min_avg
    ]


print_students(groupmates)  # Вывод общего списка студентов
try:
    threshold = float(input("\n\nВведите минимальный средний балл: "))
except ValueError:
    print("Ошибка: необходимо ввести число!")
else:
    filtered = filter_students_by_avg(groupmates, threshold)
    if filtered:
        print(f"\nСтуденты со средним баллом >= {threshold}:")
        print_students(filtered)  # Вывод списка студентов после фильтрации
    else:
        print(f"\nНет студентов со средним баллом >= {threshold}.")
