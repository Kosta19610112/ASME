def extract_lines_down(filename, i, n):
    """
    Формирует текст из строк i, i+1, ..., i+n-1 из файла.

    :param filename: Имя текстового файла.
    :param i: Номер первой строки (i >= 1).
    :param n: Количество строк для извлечения.
    :return: Сформированный текст.
    """
    try:
        # Открываем файл и читаем строки
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Преобразуем индекс i из "человеческого" в индекс Python
        start_index = i

        # Получаем нужные строки
        selected_lines = lines[start_index:start_index + n]

        # Формируем текст
        result_text = "".join(selected_lines).strip()

        # Записываем результат в файл
        with open("output.txt", 'w', encoding='utf-8') as output_file:
            output_file.write(result_text)

        print("Сформированный текст записан в 'output.txt'.")
        return result_text

    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

list_i = [21936, 22120, 22318, 22500, 22698, 22898, 23076, 23262, 23446, 23624, 23808, 23986, 24170, 24352, 24532, 24712, 
 24890, 25068, 25246, 25442, 25622, 25806, 25916]
len0 =  23

for j in range(22, 23):
    i = list_i[j]
    n = 7
    res_text = extract_lines_down('initialASME.txt', i, n)
    print(res_text)

    filename = 'tablica2A' + '_' + str(i) + '.txt'
    file = open(filename, 'w')
    file.write(res_text)
    file.close()
