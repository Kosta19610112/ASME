def read_blocks(filename):
    """
    Считывает из файла блоки по 5 строк, начиная с 3-й строки, пропуская каждые 5 строк, 
    и записывает их в файл 'result.txt'.

    :param filename: Имя входного файла.
    """
    try:
        blocks = []  # Список для хранения блоков текста

        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()  # Считываем все строки файла

        start = 2  # Индекс начала (3-я строка, индекс 2)
        while start < len(lines):
            # Считываем блок из 5 строк
            block = lines[start:start + 5]
            # Преобразуем блок в текст
            block_text = "".join(block).strip()
            blocks.append(block_text)
            # Переходим на следующую группу строк
            start += 10  # Переход на строку с номером на 5 больше последней

        # Записываем результат в файл
        with open('result.txt', 'w', encoding='utf-8') as result_file:
            for i, block in enumerate(blocks, start=1):
                result_file.write(f"Блок {i}:\n{block}\n\n")

        print("Результаты записаны в файл 'result.txt'.")
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

filename = 'result.txt'
read_blocks(filename)