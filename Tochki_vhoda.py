import pandas as pd

# Укажите путь к исходному текстовому файлу
input_file_path = 'initialASME.txt'

# Чтение данных из текстового файла
with open(input_file_path, 'r') as file:
    lines = file.readlines()

# Инициализация списка для хранения номеров строк с заголовками
head1 = []

# Целевая строка для поиска
header_line = '40 65 100 125 150 200 250 300 325 350 375 400 425 450 475 500'

# Поиск строк с целевым текстом
for index, line in enumerate(lines):
#    if line.strip() == header_line:
#    if line == header_line:
    if header_line in line:
        head1.append(index)

print(f"Строки с заголовком найдены на следующих номерах: {head1}")

f = open('head_numbers.txt', 'w')
print(head1, file = f)
print('len = ', len(head1), file = f)
f.close()
