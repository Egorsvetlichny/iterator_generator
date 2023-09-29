d = [5, 3, 7, 10, 32]
it = iter(d)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# слудующий print(next(it)) вызовет ошибку StopIteration т.к. достигнут конец списка

s = 'python'
it = iter(s)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# слудующий print(next(it)) вызовет ошибку StopIteration т.к. достигнут конец строки

r = range(5)
it = iter(r)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# слудующий print(next(it)) вызовет ошибку StopIteration т.к. достигнут конец range

# цикл for реализует итератор протокол, не вызывая ошибку StopIteration