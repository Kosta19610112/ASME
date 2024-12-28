def compare_files_line_by_line(file1, file2):
    try:
        with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
            for line1, line2 in zip(f1, f2):
                if line1 != line2:
                    print("Файлы различаются.")
                    return
            # Проверка на случай, если один файл длиннее другого
            if f1.read() or f2.read():
                print("Файлы различаются.")
            else:
                print("Файлы одинаковые.")
    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Пример использования
compare_files_line_by_line('dffin.csv', 'dffin1.csv')
