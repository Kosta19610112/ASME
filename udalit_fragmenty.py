def filter_lines(input_file, output_file, ranges):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()
    
    exclude = set()
    for start, end in ranges:
        exclude.update(range(start, end + 1))
    
    with open(output_file, 'w') as outfile:
        for idx, line in enumerate(lines, start=1):  # Нумерация строк начинается с 1
            if idx not in exclude:
                outfile.write(line)

# Пример использования
L = [(2, 4), (4, 5), (7, 9)]
input_filename = 'text.txt'     #'initialASME.txt'
output_filename = 'udal_frag.txt'   #'udal_frag_ASME.txt'

filter_lines(input_filename, output_filename, L)
