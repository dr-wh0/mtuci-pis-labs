
var groupmates = [
    {
        "name": "Александр",
        "surname": "Шалавасов",
        "group": "БСТ2202",
        "marks": [5, 5, 5]
    },
    {
        "name": "Серафим",
        "surname": "Сухарев",
        "group": "БСТ2202",
        "marks": [4, 5, 5]
    },
    {
        "name": "Павел",
        "surname": "Черниговский",
        "group": "БСТ2202",
        "marks": [3, 4, 5]
    },
    {
        "name": "Алексей",
        "surname": "Обласов",
        "group": "БВТ2201",
        "marks": [5, 4, 5]
    },
    {
        "name": "Даниил",
        "surname": "Кудряшов",
        "group": "БИН2203",
        "marks": [3, 4, 4]
    },
    {
        "name": "Глеб",
        "surname": "Степанов",
        "group": "БИК2205",
        "marks": [5, 5, 3]
    },
    {
        "name": "Юрий",
        "surname": "Алексанов",
        "group": "БСТ2204",
        "marks": [3, 5, 5]
    }
];

console.log(groupmates);

console.log('\n\n\n');

var rpad = function (str, length) {
    // js не поддерживает добавление нужного количества символов
    // справа от строки, т.е. аналога ljust из Python здесь нет
    str = str.toString(); // преобразование в строку
    while (str.length < length)
        str = str + ' '; // добавление пробела в конец строки
    return str; // когда все пробелы добавлены, возвратить строку
};

var getAverageMark = function (marks) {
    var sum = 0;
    for (var i = 0; i < marks.length; i++)
        sum += marks[i];
    return sum / marks.length;
};


var printStudents = function (students) {
    console.log(
        rpad("Имя", 15),
        rpad("Фамилия", 15),
        rpad("Группа", 8),
        rpad("Оценки", 20)
    );
    // был выведен заголовок таблицы
    for (var i = 0; i <= students.length - 1; i++) {
        var avg = getAverageMark(students[i].marks).toFixed(2);
        // в цикле выводится каждый экземпляр студента
        console.log(
            rpad(students[i]['name'], 15),
            rpad(students[i]['surname'], 15),
            rpad(students[i]['group'], 8),
            rpad(students[i]['marks'], 20),
            rpad(avg, 13)
        );
    }
    console.log('\n'); // добавляется пустая строка в конце вывода
};

var filterByGroup = function (students) {
    var groupName = prompt("Введите группу для фильтрации:");
    if (!groupName) return students;

    var filtered = students.filter(function (s) {
        return s.group === groupName;
    });

    if (filtered.length === 0)
        console.log("Студентов из группы " + groupName + " не найдено.\n");

    return filtered;
};

var filterByAvgMark = function (students) {
    var input = prompt("Введите минимальный средний балл:");
    if (!input) return students;

    var minAvg = parseFloat(input);
    var filtered = students.filter(function (s) {
        return getAverageMark(s.marks) > minAvg;
    });

    if (filtered.length === 0)
        console.log("Нет студентов со средним баллом выше " + minAvg + ".\n");

    return filtered;
};

printStudents(groupmates);                    // вывод всех студентов
var byGroup = filterByGroup(groupmates);
if (byGroup.length === 0)
    byGroup = groupmates;
console.log("Студенты, отфильтрованные по группе:\n");
printStudents(byGroup);                       // фильтрация по группе
console.log("Студенты, отфильтрованные также по среднему баллу:\n");
printStudents(filterByAvgMark(byGroup));      // фильтрация по среднему баллу
