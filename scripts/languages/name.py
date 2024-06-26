import random
from scripts.shared import read_lines_from_file

def get_next_syllable(lang: str) -> str:
    groups = {}
    types = []
    file_lines = read_lines_from_file(f'../../languages/{lang}.txt')
    for line in file_lines:
        if line.find(':') > -1:
            if line.find(':') == 1:
                if len(line[2:].lstrip().split(' ')) > 1:
                    groups[line[0]] = line[2:].lstrip().split(' ')
                else:
                    groups[line[0]] = []
                    for c in line[2:].lstrip():
                        if c.isupper():
                            groups[line[0]] += groups[c]
                        else:
                            groups[line[0]].append(c)
            else:
                raise ValueError('Invalid group definition: ' + line[:line.find(':')])
        elif len(line) > 0:
            types.append(line)
    doutput = types[random.randint(0, len(types) - 1)]
    output = ''
    for c in doutput:
        if c.isupper():
            output += groups[c][random.randint(0, len(groups[c]) - 1)]
        else:
            output += c
    return output

def create_name(lang: str) -> str:
    output = ''
    num_syllables = 3#random.randint(1, 3)
    for i in range(num_syllables):
        output += get_next_syllable(lang)
    return output[0].upper() + output[1:]

if __name__ == '__main__':
    try:
        for _ in range(10):
            print(create_name('gothic'))
    except KeyError as e:
        print(f'Group {e} not found')
    except FileNotFoundError as e:
        print(f'File not found: {e.filename}')
    except ValueError as e:
        print(e)
