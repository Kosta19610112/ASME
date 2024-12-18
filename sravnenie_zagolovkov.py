import os

def read_files(file_list):
    """Считать содержимое каждого файла из списка и вернуть список текстов."""
    texts = []
    for file_path in file_list:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                texts.append(text)
        except FileNotFoundError:
            print(f"Файл {file_path} не найден.")
        except Exception as e:
            print(f"Ошибка при чтении файла {file_path}: {e}")
    return texts



def read_files_ignore_errors(file_list):
    """Считать содержимое файлов, игнорируя ошибки кодировки."""
    texts = []
    for file_path in file_list:
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                text = file.read()
                texts.append(text)
        except Exception as e:
            print(f"Ошибка при чтении файла {file_path}: {e}")
    return texts



file_list = []

def list_all_files(directory):
    """Сформировать список всех файлов в заданной директории и вложенных папках."""
    all_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            all_files.append(os.path.join(root, file))
    return all_files


directory = r'c:\Users\ksree\Documents\Git\ASME\Head'

if os.path.isdir(directory):
    files = list_all_files(directory)
    print(f"Найдено {len(files)} файлов:")
    for file in files:
        file_list.append(file)
else:
    print("Указанный путь не является директорией.")


texts = read_files_ignore_errors(file_list)

s = set(texts)
print(s)
