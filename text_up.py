def extract_lines_up(filename, i, n):
    """
    Формирует текст из строк i, i-1, ..., i-n+1 из файла, записывая их в обратном порядке.

    :param filename: Имя текстового файла.
    :param i: Номер последней строки (i >= 1).
    :param n: Количество строк для извлечения.
    :return: Сформированный текст в обратном порядке.
    """
    try:
        # Чтение всех строк из файла
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Преобразуем i в индекс Python (от 0)
        end_index = i
        start_index = max(end_index - n + 1, 0)  # Учитываем границы файла

        # Извлекаем строки от i до i-n+1
        selected_lines = lines[start_index:end_index + 1]

        # Записываем строки в обратном порядке
        reversed_lines = selected_lines[::-1]

        # Формируем итоговый текст
        result_text = "".join(reversed_lines).strip()

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
n = 5
for j in range(len(list_i)):
    i = list_i[j]
    res_text = extract_lines_up('initialASME.txt', i, n)
    print(res_text)

    filename = 'head2A' + '_' + str(i) + '.txt'
    file = open(filename, 'w')
    file.write(res_text)
    file.close()