"""Вывод списка студентов группы с информацией о результатах экзаменов

- print_students: Вывод списка студентов группы с информацией об экзаменах.
- filter_students_by_avg: Фильтрация студентов по среднему баллу.
"""


groupmates = [
    {
        "name": "Дмитрий",
        "surname": "Шагаров",
        "exams": ["История", "ОС", "КТП"],
        "marks": [4, 5, 5]
    },
    {
        "name": "Никита",
        "surname": "Шулапов",
        "exams": ["Философия", "КТП", "АиГ"],
        "marks": [5, 3, 4]
    },
    {
        "name": "Максим",
        "surname": "Соловьев",
        "exams": ["АиГ", "ОС", "Физика"],
        "marks": [5, 4, 4]
    },
    {
        "name": "Шалавасов",
        "surname": "Александр",
        "exams": ["История", "КТП", "Физика"],
        "marks": [5, 5, 4]
    },
    {
        "name": "Овчинников",
        "surname": "Павел",
        "exams": ["ИС", "Философия", "Электроника"],
        "marks": [3, 4, 4]
    },
    {
        "name": "Черниговский",
        "surname": "Павел",
        "exams": ["АиГ", "СиАОД", "КТП"],
        "marks": [5, 5, 3]
    }
]


def print_students(students):
    print(
        u"Имя".ljust(20),
        u"Фамилия".ljust(20),
        u"Экзамены".ljust(35),
        u"Оценки".ljust(20),
        u"Средний балл".ljust(20),
    )
    for student in students:
        avg_mark = sum(student["marks"]) / len(student["marks"])
        print(
            student["name"].ljust(20),
            student["surname"].ljust(20),
            str(student["exams"]).ljust(35),
            str(student["marks"]).ljust(20),
            f"{avg_mark:.2f}".ljust(20),
        )


def filter_students(students, min_avg):
    return [
        student for student in students
        if sum(student["marks"]) / len(student["marks"]) >= min_avg
    ]


print(
        u"Имя".ljust(20),
        u"Фамилия".ljust(20),
        u"Экзамены".ljust(35),
        u"Оценки".ljust(20),
        u"Средний балл".ljust(20),
    )
for student in groupmates:
    avg_mark = sum(student["marks"]) / len(student["marks"])
    print(
        student["name"].ljust(20),
        student["surname"].ljust(20),
        str(student["exams"]).ljust(35),
        str(student["marks"]).ljust(20),
        f"{avg_mark:.2f}".ljust(20),
    )
print("\n\n")
threshold = float(input("Минимальный ср. балл: "))
filtered = filter_students(groupmates, threshold)
print(f"\nСтуденты со ср. баллом >= {threshold}:")
print_students(filtered)
