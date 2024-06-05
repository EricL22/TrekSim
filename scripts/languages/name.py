import random
from scripts.shared import read_lines_from_file

def get_next_syllable(lang: str) -> str:
    groups = {}
    types = []
    file_lines = read_lines_from_file(f'../../languages/{lang}.txt')
    for line in file_lines:
        if line.find(':') > -1:
            if len(line[line.find(':')+1:].lstrip().split(' ')) > 1:
                groups[line[:line.find(':')]] = line[line.find(':')+1:].lstrip().split(' ')
            else:
                groups[line[:line.find(':')]] = []
                for c in line[line.find(':')+1:].lstrip():
                    groups[line[:line.find(':')]] += groups[c]
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
    num_syllables = random.randint(1, 3)
    for i in range(num_syllables):
        output += get_next_syllable(lang)
    return output[0].upper() + output[1:]

if __name__ == '__main__':
    try:
        for _ in range(100):
            print(create_name('stuffumanic'))
    except KeyError as e:
        print(f'Group {e} not found')
