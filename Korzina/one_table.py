import pandas as pd

def Table(input_file_path, save_number):
    output_file_path = 'output_dataframe' + '_' + str(save_number) + '.csv'
    # Чтение данных из текстового файла
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    # Первая строка - это заголовок
    header = lines[0].strip().split()

    # Остальные строки - это данные
    data = [line.strip().split() for line in lines[1:]]

    # Корректируем строки, где больше элементов, чем в заголовке
    corrected_data = [row[:len(header)] if len(row) > len(header) else row for row in data]

    # Создание DataFrame
    df = pd.DataFrame(corrected_data, columns=header)

    # Сохранение DataFrame в CSV-файл
    df.to_csv(output_file_path, index=False)

    print(f"DataFrame успешно сохранен в файл: {output_file_path}")

save_number = 1
# Укажите путь к исходному текстовому файлу
input_file_path = 'one_table.txt'
Table(input_file_path, save_number)