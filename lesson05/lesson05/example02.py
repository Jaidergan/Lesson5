"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('example02.txt') as f:
    rows = f.readlines()
    expanded_rows = [row.split() for row in rows]

rows_count = len(rows)
words_count = [len(word_list) for word_list in expanded_rows]

print(f"Всего строк - {rows_count}")
n = 0
while n < len(words_count):
    print(f"Количество слов в строке {n + 1} - {words_count[n]}")
    n += 1