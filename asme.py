import pdfplumber
import pandas as pd

# Путь к файлу PDF
file_path = 'pdf_urez.pdf'

# Открываем PDF
with pdfplumber.open(file_path) as pdf:
    # Открываем нужную страницу (например, 1)
    page = pdf.pages[0]
    
    # Извлекаем таблицу
    table = page.extract_table()
    
    # Создаем DataFrame
    df = pd.DataFrame(table[1:], columns=table[0])

# Преобразуем данные в числовой формат (если требуется)
df = df.apply(pd.to_numeric, errors='coerce')

# Выводим таблицу
print(df)
