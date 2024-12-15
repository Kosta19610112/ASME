from tabula import read_pdf
import pandas as pd

# Путь к вашему PDF-файлу
file_path = "pdf_urez.pdf"

# Извлечение таблицы
df = read_pdf(file_path, pages=1, lattice=True)  # pages=1 для первой страницы

# Преобразование данных в числовой формат
df = df.apply(pd.to_numeric, errors='coerce')

# Выводим таблицу
print(df)
