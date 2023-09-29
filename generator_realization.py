# Генератор это более удобный способ реализовать итератор протокол

def string_by_letter(string):
    for letter in string:
        yield letter.upper()


for letter in string_by_letter('Hello world!'):
    print(letter)

print()

from collections.abc import Iterator

generator = string_by_letter('Hello world!')
print(isinstance(generator, Iterator)) # Значение True, то есть генератор является наследником итератора