def poisk(text, textnot, filename):
    """
    Ищет строки в файле filename, которые совпадают с text, и записывает номера строк в файл result.txt.

    :param text: Текст для поиска.
    :param filename: Имя файла, в котором выполняется поиск.
    """
    try:
        # Список для хранения номеров строк
        line_numbers = []

        # Чтение файла и поиск совпадений
        with open(filename, 'r', encoding='utf-8') as file:
            for i, line in enumerate(file, start=1):
                if text in line and textnot not in line:
                    line_numbers.append(i)
        print(line_numbers)
        print(len(line_numbers))
        # Запись найденных номеров строк в файл
        with open('result.txt', 'w', encoding='utf-8') as result_file:
            result_file.write(f'Номера строк, содержащие "{text}":\n')
            result_file.write(", ".join(map(str, line_numbers)))
            result_file.write('\n')
            result_file.write(str(len(line_numbers)))

        print(f"Номера строк записаны в файл 'result.txt'.")
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


# Целевая строка для поиска
text = '40 65 100 125 150 200 250 300 325 350 375 400 425 450 475 500'
textnot = '40 65 100 125 150 200 250 300 325 350 375 400 425 450 475 500 ***'

text = '40 65 100 125 150 200 250 300 325 350 375 400 425 450 475'
textnot = '40 65 100 125 150 200 250 300 325 350 375 400 425 450 475 500'


filename = 'initialASME.txt'
input_file_path = input(f"[{filename}] ") or filename
print(f"Вы ввели: {input_file_path}")

poisk(text, textnot, filename)