"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

strings = []

while True:
    with open('example01.txt', 'a+') as f:
        string = input("Введите строку >>> ")

        if not string:
            break

        f.write(f"{string}\n")