import pdfplumber

def pdf2txt(start, end):
    # Укажите путь к вашему PDF файлу
    pdf_path = "extracted_pages" + '_' + str(start) + '_' + str(end) + ".pdf"

    # Открываем PDF с помощью pdfplumber
    with pdfplumber.open(pdf_path) as pdf:
        # Инициализируем переменную для хранения текста
        full_text = ""
        
        # Проходим по всем страницам
        for page_number, page in enumerate(pdf.pages, start=1):
            # Извлекаем текст страницы
            text = page.extract_text()
            if text:  # Если текст на странице найден
                full_text += f"=== Страница {page_number} ===\n{text}\n\n"
            else:
                full_text += f"=== Страница {page_number} ===\n(Текст не найден)\n\n"

    # Сохраняем текст в файл или выводим
    output_path = "output" + '_' + str(start) + '_' + str(end) + ".txt"
    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write(full_text)

    print(f"Текст успешно извлечен и сохранен в файл {output_path}")


start = int(input('start = '))
end = int(input('end = '))
pdf2txt(start, end)