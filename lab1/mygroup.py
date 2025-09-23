"""Вывод списка студентов группы с информацией о результатах экзаменов

- print_students: Вывод списка студентов группы с информацией об экзаменах.
- filter_students_by_avg: Фильтрация студентов по среднему баллу.
"""

# Список студентов группы с информацией об экзаменах
groupmates = [
    {
        "name": "Александр",
        "surname": "Шалавасов",
        "exams": ["УД", "СиАОД", "ОС"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Серафим",
        "surname": "Сухарев",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 5, 5]
    },
    {
        "name": "Павел",
        "surname": "Черниговский",
        "exams": ["АиГ", "ИС", "ОС"],
        "marks": [3, 4, 5]
    },
    {
        "name": "Алексей",
        "surname": "Обласов",
        "exams": ["ОС", "КТП", "История"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Даниил",
        "surname": "Кудряшов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [3, 4, 4]
    },
    {
        "name": "Глеб",
        "surname": "Степанов",
        "exams": ["СиАОД", "КТП", "АиГ"],
        "marks": [5, 5, 3]
    },
    {
        "name": "Юрий",
        "surname": "Алексанов",
        "exams": ["Философия", "КТП", "АиГ"],
        "marks": [3, 5, 5]
    }
]


def print_students(students: list) -> None:
    """Вывод списка всех студентов с информацией об экзаменах.

    Использует .ljust для выравнивания строк таблицы, вывод в кодировке Unicode.

    Args:
        students (list): Список студентов группы для вывода.
    """
    print(
        u"Имя".ljust(15),
        u"Фамилия".ljust(20),
        u"Экзамены".ljust(30),
        u"Оценки".ljust(20),
        u"Средний балл".ljust(15),
    )
    for student in students:
        avg_mark = sum(student["marks"]) / len(student["marks"])
        print(
            student["name"].ljust(15),
            student["surname"].ljust(20),
            str(student["exams"]).ljust(30),
            str(student["marks"]).ljust(20),
            f"{avg_mark:.2f}".ljust(15),
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


if __name__ == "__main__":
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
