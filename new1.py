def poisk(text, filename):
    """
    Ищет строки в файле filename, содержащие text, записывает номера строк в файл, 
    а также текст 5 строк выше совпадений в один текстовый блок.

    :param text: Текст для поиска.
    :param filename: Имя файла, в котором выполняется поиск.
    """
    try:
        # Список для хранения результатов
        results = []

        # Чтение файла в список строк
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Поиск совпадений
        for i, line in enumerate(lines, start=1):
            if text in line:
                # Номер строки, где найден текст
                results.append(f"Строка {i}: {line.strip()}")
                # 5 строк выше, если они есть
                start_index = max(0, i - 6)  # Начало блока, учитывая границы файла
                context = "".join(lines[start_index:i]).strip()
                results.append(f"Контекст (5 строк выше):\n{context}\n")

        # Запись результатов в файл
        with open('result.txt', 'w', encoding='utf-8') as result_file:
            result_file.write("\n".join(results))

        print("Результаты записаны в файл 'result.txt'.")
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


# Целевая строка для поиска
text = '40 65 100 125 150 200 250 300 325 350 375 400 425 450 475 500'
filename = 'initialASME.txt'
poisk(text, filename)