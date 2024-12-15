import os

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

if __name__ == "__main__":
    pdf_files = list_pdf_files()
    if pdf_files:
        print("Список PDF-файлов:")
        for pdf in pdf_files:
            print(pdf)
    else:
        print("PDF-файлы не найдены.")
