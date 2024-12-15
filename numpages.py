import pandas as pd
from PyPDF2 import PdfReader
import fitz  # PyMuPDF
import pdfplumber
from pdfminer.high_level import extract_pages
from PyPDF4 import PdfFileReader
import time
import os


def count_pages_all_methods(pdf_path):
    results = []

    t0 = time.time()
    # Метод 1: PyPDF2
    try:
        reader = PdfReader(pdf_path)
        l = len(reader.pages)
    except Exception as e:
        print(f"Ошибка в PyPDF2 ({pdf_path}): {e}")
        l = None

    t1 = time.time()
    results.append((l, f'{t1 - t0:.2f}'))

    # Метод 2: PyMuPDF (fitz)
    try:
        doc = fitz.open(pdf_path)
        l = doc.page_count
    except Exception as e:
        print(f"Ошибка в PyMuPDF ({pdf_path}): {e}")
        l = None

    t2 = time.time()
    results.append((l, f'{t2 - t1:.2f}'))
    # Метод 3: pdfplumber
    try:
        with pdfplumber.open(pdf_path) as pdf:
            l = len(pdf.pages)
    except Exception as e:
        print(f"Ошибка в pdfplumber ({pdf_path}): {e}")
        l = None

    t3 = time.time()
    results.append((l, f'{t3 - t2:.2f}'))
    # Метод 4: PDFMiner
    try:
        print(1/0)
        num_pages = sum(1 for _ in extract_pages(pdf_path))
        l = num_pages
    except Exception as e:
        print(f"Ошибка в PDFMiner ({pdf_path}): {e}")
        l = None

    t4 = time.time()
    results.append((l, f'{t4 - t3:.2f}'))
    # Метод 5: PyPDF4
    try:
        with open(pdf_path, 'rb') as f:
            reader = PdfFileReader(f)
            l = reader.numPages
    except Exception as e:
        print(f"Ошибка в PyPDF4 ({pdf_path}): {e}")
        l = None
    t5 = time.time()
    results.append((l, f'{t5 - t4:.2f}'))
    return tuple(results)

def list_pdf_files():
    # Получаем текущую директорию, где находится скрипт
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Формируем путь к поддиректории PDF
    pdf_directory = os.path.join(script_directory, 'PDF')

    # Проверяем, существует ли поддиректория PDF
    if not os.path.exists(pdf_directory):
        print(f"Поддиректория 'PDF' не найдена: {pdf_directory}")
        return []

    # Составляем список полных путей к PDF-файлам
    pdf_files = [os.path.join(pdf_directory, file) for file in os.listdir(pdf_directory) if file.endswith('.pdf')]

    return pdf_files


pdf_files = list_pdf_files()



# Создание общего списка
results_list = []
for pdf_file in pdf_files:
    pdf_short = os.path.basename(pdf_file)
    page_counts = count_pages_all_methods(pdf_file)
    results_list.append((pdf_short, *page_counts))

# Создание DataFrame
columns = ["File Name", "PyPDF2", "PyMuPDF", "pdfplumber", "PDFMiner", "PyPDF4"]
df = pd.DataFrame(results_list, columns=columns)

# Сохранение DataFrame в CSV (если нужно)
try:
    df.to_csv("pdf_page_counts.csv", index=False, encoding = 'utf-8-sig')
except:
    df.to_csv("pdf_page_counts1.csv", index=False, encoding = 'utf-8-sig')

# Вывод DataFrame
print(df)

