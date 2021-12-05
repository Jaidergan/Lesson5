"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб)
Физика: 30(л) - 10(лаб)
Физкультура: - 30(пр) -
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

subjects = {}

with open('example06.txt') as f:
    for row in f:
        subject_info = row.split()
        name = subject_info[0].rstrip(':')
        subjects[name] = subject_info[1:]

result = {}

for key, value in subjects.items():
    result[key] = sum(
        [
            int(hours[:hours.index('(')])
            for hours in value
            if hours != '-'
        ]
    )

print(result)