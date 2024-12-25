import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import fitz  # PyMuPDF
import pdfplumber
from PyPDF2 import PdfReader, PdfWriter
from PyPDF4 import PdfFileReader, PdfFileWriter
from pdfminer.high_level import extract_text
import os
import time 

def dejstvie(file_pdf, programma_obrabotki, method_obrabotki):
    try:
        if programma_obrabotki == 'PyPDF2':  # PyPDF2
            if method_obrabotki == 1:  # Извлечь текст
                reader = PdfReader(file_pdf)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()
                save_result("output_text.txt", text)
            elif method_obrabotki == 4:  # Урезать документ
                writer = PdfWriter()
                reader = PdfReader(file_pdf)
                start_page, end_page = 0, 2  # Пример диапазона страниц
                for i in range(start_page, end_page):
                    writer.add_page(reader.pages[i])
                save_result("output_trimmed.pdf", writer, is_pdf=True)
        
        elif programma_obrabotki == 'PyMuPDF (fitz)':  # PyMuPDF (fitz)
            
            pdf = fitz.open(file_pdf)
            if method_obrabotki == 1:  # Извлечь текст
                text = ""
                for page in pdf:
                    text += page.get_text()
                save_result("output_text.txt", text)
            elif method_obrabotki == 3:  # Извлечь рисунки
                for page_num in range(len(pdf)):
                    page = pdf[page_num]
                    for img_index, img in enumerate(page.get_images(full=True)):
                        xref = img[0]
                        base_image = pdf.extract_image(xref)
                        image_bytes = base_image["image"]
                        image_filename = f"output_image_page{page_num + 1}_img{img_index + 1}.png"
                        with open(image_filename, "wb") as f:
                            f.write(image_bytes)
            else:
                start_page = int(input('start_page = '))
                end_page = int(input('end_page = '))
                doc = pdf 
                output_pdf = 'pdf_urez.pdf'

                # Создаем новый PDF-документ
                new_doc = fitz.open()

                # Добавляем страницы из указанного диапазона
                for page_num in range(start_page - 1, end_page):
                    new_doc.insert_pdf(doc, from_page=page_num, to_page=page_num)

                # Сохраняем новый PDF
                new_doc.save(output_pdf)
                new_doc.close()

                print(f"Страницы с {start_page} по {end_page} сохранены в {output_pdf}.")

            pdf.close()

 
        elif programma_obrabotki == 'pdfplumber':  # pdfplumber
            with pdfplumber.open(file_pdf) as pdf:
                if method_obrabotki == 1:  # Извлечь текст
                    text = "".join([page.extract_text() for page in pdf.pages])
                    save_result("output_text.txt", text)
                elif method_obrabotki == 2:  # Извлечь таблицы
                    for page_num, page in enumerate(pdf.pages):
                        tables = page.extract_tables()
                        for table_num, table in enumerate(tables):
                            save_result(f"output_table_page{page_num + 1}_table{table_num + 1}.txt", str(table))

        elif programma_obrabotki == 'PyPDF4':  # PyPDF4
            if method_obrabotki == 4:  # Урезать документ
                reader = PdfFileReader(file_pdf)
                writer = PdfFileWriter()
                start_page, end_page = 0, 2  # Пример диапазона страниц
                for i in range(start_page, end_page):
                    writer.add_page(reader.getPage(i))
                save_result("output_trimmed.pdf", writer, is_pdf=True)

        elif programma_obrabotki == 'PDFMiner':  # PDFMiner
            if method_obrabotki == 1:  # Извлечь текст
                text = extract_text(file_pdf)
                save_result("output_text.txt", text)

    except Exception as e:
        print(f"Ошибка обработки: {str(e)}")

def save_result(filename, content, is_pdf=False):
    if is_pdf:
        with open(filename, "wb") as file:
            content.write(file)
    else:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)



def Pusk():
    # Получаем введённое имя файла и выбранный метод обработки
#    file_name = entry_file_name.get()
    file_name = entry_file_path.get()

    selected_method = combo_methods.get()
    
    # Проверяем, введено ли имя файла и выбран ли метод
    if not file_name:
        messagebox.showerror("Ошибка", "Введите имя файла!")
        return
    if not selected_method:
        messagebox.showerror("Ошибка", "Выберите метод обработки!")
        return
    
    # Выводим информацию о файле и методе обработки
    result_message = f"Имя файла: {file_name}\nМетод обработки: {selected_method}"
    messagebox.showinfo("Информация", result_message)

    print('1 - text')
    print('2 - tables')
    print('3 - figures')
    print('4 - cut')
    time0 = time.time()
    what_to_do = int(input('what_to_do = '))
    dejstvie(file_name, selected_method, what_to_do)
    time1 = time.time()
    print('Время обработки = ', time1 - time0)


def select_file():
    # Открывает диалоговое окно для выбора файла
    filepath = filedialog.askopenfilename(
        title="Выберите PDF файл",
        filetypes=[("PDF файлы", "*.pdf")])
    
    filename = 'default_pdf'
    file = open(filename, 'w')
    file.write(filepath)
    file.close()
    if filepath:
        entry_file_path.delete(0, tk.END)  # Очищает текущее содержимое поля
        entry_file_path.insert(0, filepath)  # Вставляет выбранный путь в поле

def show_selected_file():
    filepath = entry_file_path.get()
    if filepath:
        messagebox.showinfo("Выбранный файл", f"Вы выбрали файл:\n{filepath}")
    else:
        messagebox.showerror("Ошибка", "Файл не выбран!")

def all_pdf():
    # Определяем путь к текущему файлу
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Указываем относительный путь к поддиректории с PDF-файлами
    pdf_dir = os.path.join(current_dir, 'PDF')

    # Проверяем, существует ли директория
    if not os.path.exists(pdf_dir):
        print(f"Директория {pdf_dir} не существует.")
    else:
        # Получаем список всех PDF-файлов в поддиректории
        pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]

        # Выводим список файлов
        if pdf_files:
            pass
        else:
            print("В поддиректории нет PDF-файлов.")
    return pdf_files


pdf_list = all_pdf()
print('Все pdf-файлы : ', pdf_list)

#default_pdf = r"C:\Users\ksree\Documents\GitHub\Parsing\Predvar_rabota_s_dok\PDF\pdf_urez.pdf"
filename = 'default_pdf'
file = open(filename)
txt = file.read()
file.close() 
default_pdf = txt

# Создание основного окна
root = tk.Tk()
root.title("Интерфейс обработки PDF")

# Поле для ввода имени файла вручную
frame_file = tk.Frame(root)
frame_file.pack(pady=10)
tk.Label(frame_file, text="Введите имя файла:").pack(side=tk.LEFT, padx=5)

# Поле для текста с дефолтным значением
entry_file_path = tk.Entry(frame_file, width=50)
entry_file_path.insert(0, default_pdf)  # Устанавливает значение по умолчанию
entry_file_path.pack(side=tk.LEFT, padx=5)

# Кнопка для вызова браузера файлов
btn_browse = tk.Button(frame_file, text="Обзор...", command=select_file)
btn_browse.pack(side=tk.LEFT, padx=5)
#default_pdf = 
# Кнопка для подтверждения выбора файла

btn_show = tk.Button(root, text="Показать выбранный файл", command=show_selected_file)
btn_show.pack(pady=20)

frame_method = tk.Frame(root)
frame_method.pack(pady=10)

tk.Label(frame_method, text="Выберите метод обработки:").pack(side=tk.LEFT, padx=5)
combo_methods = ttk.Combobox(
    frame_method, 
    values=["PyPDF2", "PyMuPDF (fitz)", "pdfplumber", "PyPDF4", "PDFMiner"],
    state="readonly",
    width=20
)
combo_methods.pack(side=tk.LEFT, padx=5)

# Кнопка для запуска программы Pusk
btn_run = tk.Button(root, text="Запуск", command=Pusk)
btn_run.pack(pady=20)



  # Запуск интерфейса
print('Запуск')
root.mainloop()
