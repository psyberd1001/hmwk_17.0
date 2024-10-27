from typing import Dict, Any, TextIO


def custom_write(file_name, strings):
    strings_positions = {}
    values = [0]
    file = open(file_name, 'w', encoding='utf-8')
    for i in strings:
        file.write(f'{i}\n')
        values.append(file.tell())
    del values[-1]
    print(values)
    strings_positions = dict(zip(values, strings))
    print(strings_positions)
    file.close()


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

custom_write('1test.txt', info)
