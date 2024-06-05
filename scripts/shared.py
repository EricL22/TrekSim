def read_lines_from_file(file_path, encoding: str = 'utf-8'):
    with open(file_path, 'r', encoding=encoding) as the_file:
        for line in the_file:
            yield line.rstrip()
