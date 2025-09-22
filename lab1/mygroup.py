""" Вывод списка студентов группы с информацией о результатах экзаменов

- print_students: Вывод списка студентов группы с информацией об экзаменах.
"""

from typing import List

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


def print_students(students: List):
    """Вывод списка всех студентов с информацией об экзаменах.

    Использует .ljust для выравнивания строк таблицы, вывод в кодировке Unicode.

    Args:
        students (List): Список студентов группы для вывода.
    """
    print(
        u"Имя".ljust(15),
        u"Фамилия".ljust(20),
        u"Экзамены".ljust(30),
        u"Оценки".ljust(20),
    )
    for student in students:
        print(
            student["name"].ljust(15),
            student["surname"].ljust(20),
            str(student["exams"]).ljust(30),
            str(student["marks"]).ljust(20),
        )


print_students(groupmates)
