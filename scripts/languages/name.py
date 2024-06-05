import random

def get_next_syllable() -> str:
    return 'A'

def create_name() -> str:
    output = ''
    num_syllables = random.randint(1, 3)
    for i in range(num_syllables):
        output += get_next_syllable()
    return output[0].upper() + output[1:]

if __name__ == '__main__':
    print(create_name())
