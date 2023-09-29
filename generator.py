def test1():
    for i in range(3):
        yield i


a = test1()
print(a)  # объект "а" является генератором
print(next(a))
print(next(a))
print(next(a))
# слудующий print(next(a)) вызовет ошибку StopIteration т.к. достигнут конец range


# более короткая запись того же генератора
def test2():
    yield from [0, 1, 2]


a = test2()
print(a)  # объект "а" является генератором
print(next(a))
print(next(a))
print(next(a))
# слудующий print(next(a)) вызовет ошибку StopIteration т.к. достигнут конец списка


# для реализации генератора можно использовать list comprehension
def test3():
    yield [x for x in range(20)]


for i in test3():
    print(i)


# использование нескольких yield
def test4():
    print('started')
    while True:
        yield 1
        yield 2
        yield 3


a = test4()
print(a)  # объект "а" является генератором
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))


# метод send() позволяет отправлять события в генератор
def test5():
    print('started')
    while True:
        x = yield
        print('recv:', x)


a = test5()
next(a)  # выведет в консоль 'started'
next(a)  # выведет в консоль 'None', т.к. мы не использовали метод send()
a.send('test')  # выведет в консоль 'test'
a.send('Hello, world!')  # выведет в консоль 'Hello world!'

# Используя метод send() мы можем передавать события в yield
# и как-либо влиять на нашу функцию.
# Такой подход удобно использовать при решении ресурсозатратных задач.