def extract_lines_down0(filename, i, n):
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
        start_index = i - 1

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

list_i = [21937, 22121, 22319, 22501, 22699, 22899, 23077, 23263, 23447, 23625, 23809, 23987, 
          24171, 24353, 24533, 24713, 24891, 25069, 25247, 25443, 25623, 25807, 25917]
len0 =  23

#"40 65 100 125 150 200 250 300 325 350 375 400 425 450 475"
list_i =  [5493, 5725, 5960, 6192, 6420, 6648, 6876, 7104, 7332, 7560, 7788, 8016, 8244, 
           8472, 8700, 8929, 9174, 9419, 9648, 9876, 10105, 10335, 10564, 10792, 11020, 
           11248, 11476, 11709, 11942, 12170, 12399, 12628, 12856, 13084, 13312, 13543, 
           13774, 13949]
len0 = 38

#for j in range(0, len0-1):
for j in range(len0-1, len0):
    i = list_i[j]
    n = 19
#    n = 46
    res_text = 0('initialASME.txt', i, n)
    print(res_text)

    filename = 'Table 1A' + '_' + str(i) + '.txt'
    file = open(filename, 'w')
    file.write(res_text)
    file.close()









def extract_lines_down(filename, list_i, n):
    for i in list_i:
        extract_lines_down0(filename, i, n)

filename = 'text.txt'
list_i = = [21937, 22121, 22319, 22501, 22699, 22899, 23077, 23263, 23447, 23625, 23809, 23987, 
          24171, 24353, 24533, 24713, 24891, 25069, 25247, 25443, 25623, 25807, 25917]
extract_lines_down(filename, list_i, n)