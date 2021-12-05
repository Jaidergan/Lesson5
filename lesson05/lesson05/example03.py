"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""

with open("example03.txt") as f:
    worker_list = [worker_line.split() for worker_line in f.readlines()]

workers_with_info = [
    {"name": worker[0], "salary": float(worker[1])}
    for worker in worker_list
    if len(worker) > 1
]

salary_all = 0
numbers_worker = 0

for worker in workers_with_info:
    if worker['salary'] < 20_000:
        print(f"Фамилия сотрудника: {worker['name']}, его оклад: {worker['salary']}")
    salary_all +=  worker['salary']
    numbers_worker += 1


print(f"Средний оклад среди всех сотрудников: {salary_all / numbers_worker}")

