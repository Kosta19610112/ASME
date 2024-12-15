import pdfplumber
import pandas as pd

# Путь к вашему PDF-файлу
file_path = 'pdf_urez.pdf'

# Открываем PDF-файл
with pdfplumber.open(file_path) as pdf:
    # Указываем страницу, где находится таблица
    page = pdf.pages[0]  # Замените 0 на номер страницы (начинается с 0)
    
    # Извлекаем таблицу
    table = page.extract_table()
    # Извлекаем текст всей страницы
    text = page.extract_text()

# Анализируем текст для разделения по строкам и колонкам
    print(text)  # Вывод текста для анализа
    filename  = 'text.txt'
    f = open(filename, 'w')
    f.write(text)
    f.close()

    
    # Преобразуем таблицу в DataFrame
    if table:
        # Преобразуем таблицу в DataFrame
        df = pd.DataFrame(table[1:], columns=table[0])  # table[0] содержит заголовки
        
        # Преобразуем строки в числовой формат, если необходимо
        df = df.apply(pd.to_numeric, errors='coerce')
    else:
        print("Таблица не найдена.")

# Выводим таблицу
print(df)
