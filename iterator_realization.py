# Данный итератор реализует вывод каждой буквы строки в верхнем регистре.

class StringByLetter:
    def __init__(self, string):
        self.string = string
        self.string_len = len(string)
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if 0 <= self.position < self.string_len:
            letter = self.string[self.position]
            self.position += 1
            return letter.upper()
        raise StopIteration


for letter in StringByLetter('Hello world!'):
    print(letter)
