## Расширенные возможности

#Декораторы, Итераторы, Генераторы, Дескрипторы

### Декораторы

# Декоратор — функция, которая принимает другую функцию и возвращает функцию обертку

def trace(func):
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)
    return inner

@trace
def foo(x):
    return 42

foo = trace(foo)

foo(1)

def memoized(func):
    cache = {}
    def inner(x):
        key = x
        if key not in cache:
            print("Calculate new value")
            cache[key] = func(x)
        return cache[key]
    return inner

@memoized
def identity(x):
    "I do nothing useful."
    return x

identity(1)
identity(2)
identity(1)

# Модуль functools.lru_cache

#### Декораторы с аргументами
def trace_arg(handle):
    print("Sart trace_arg")
    def wrapper(func):
        print("Start wrapper")
        def inner(*args, **kwargs):
            print(func.__name__, args, kwargs, file=handle)
            return func(*args, **kwargs)
        return inner
    return wrapper

import sys
@trace_arg(sys.stdout)
def hello(who="obody"):
    print("Hi " + who)

hello("me")


#### Свойства с помощью декоратора
class Decor:
    def __init__(self, value):
        self._data = value

    @classmethod
    def classmethod(cls):
        print("Class: ", cls)

    @staticmethod
    def static():
        print("Hello static")

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, v):
        self._data = v


d = Decor(3)
d.data
d.classmethod()
d.static()
Decor.static()
d._data
d.data = 2


### Итераторы
# Для унификации работы с последовательностями содзан специальный протокол.
# Объект реализующий этот протокол называется "Итератор"
# Итератор это класс реализующй методы __iter__() и __next__()
# итераторы файлов
# итераторы встроенных типов

import random
class MyRandomIterator():
    def __init__(self, a):
        self.amount = a
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.amount:
            self.counter += 1
            return random.random()
        raise StopIteration



LI = MyRandomIterator(2)
type(LI)
LI.__next__()
LI.__next__()
LI.__next__()

#работа с элементами массива с помощью цикла
for l in MyRandomIterator(3):
    print(l)


### Генераторы

# Генераторное выражение
(i for i in [1,2])

def sequence_gen(n):
    c = 0
    while c < n:
        yield c
        c += 1

for i in sequence_gen(3):
    print(i)

## Генераторы в виде функции
def skip_comments(filename, mode='r', comment='#'):
    print("*** generator is called the first time")
    for line in open(filename, mode):
        if line.startswith(comment):
            continue
        yield line
    print("*** generator is called the last time")


for line in skip_comments("lessons/examples/fox.txt"):
    print(line.strip())

sc = skip_comments("lessons/examples/fox.txt")
sc.__next__()


### Дескрипторы
# Дескриптор — это: экземпляр класса, реализующего протокол дескрипторов
# Функции протокола __get__, __set__, __delete__
class NonNegative:
    def __init__(self, value):
        self.value = value
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        assert value >= 0, "non-negative value required"
        self.value = value
    def __delete__(self, instance):
        self.value = None


class VerySafe:
    x = NonNegative(1)
    y = NonNegative(2)

very_safe = VerySafe()
very_safe.x = 42
very_safe.x
very_safe.x = -42


## Модули и пакеты

# Общая картина
#  - Повторное использование программного кода
#  - Разделение системы пространств имен
#  - Реализация служб или данных для совместного пользования

### Использование модулей или пакетов
# https://docs.python.org/3/library/os.html
import os
from os import path
from os import path as p

import email
from email.mime import image
from email.mime import audio as ad

# Модуль - это файл
# Пути поиска пакетов и модулей
import sys

sys.path

#### Переменаня окружения PYTHONPATH
# каталог site-packages
# Файлы описания пути *.pth внутри site-packages

#### Модуль site
# https://docs.python.org/3/library/site.html
import site

site.USER_SITE

### Основы программирования модулей
# создание модулей

os.getcwd()
os.chdir("lessons/examples")
sys.path.append(".")

# Пакеты модулей
# __init__.py
import mypackage
import mypackage.work

mypackage.work.action
mypackage.work.action()


### Дополнительные возможности модулей
def tester():
    print('It’s tester...')


if __name__ == '__main__':  # Только когда запускается,
    tester()  # а не импортируется

# Импортирование модулей по имени в виде строки    __import__(modname)
modname = 'mypackage'
try:
    mymodule = __import__(modname)
except ImportError:
    pass
mymodule

# перезагрузка модулей
import importlib

importlib.reload(mypackage)

### Создание пакета для установки
# setup.py
# Создание архива для распространения sdist
# python setup.py sdist

# pip install .
# pip install -e .
# pip uninstall module

# запуск скрипта как модуля
# Создать файл __main__.py в модуле
# python -m python -m script
#> python -m http.server 8000

# Форматы пакетов: egg, wheel

"""
Материал для дополнительного изучения:

Итерируемый объект, итератор и генератор
https://habrahabr.ru/post/337314/  

Генераторы
http://www.dabeaz.com/finalgenerator/

Понимаем декораторы в Python'e, шаг за шагом.
http://habrahabr.ru/post/141411/
http://habrahabr.ru/post/141501/

Python Descriptors Demystified
http://nbviewer.ipython.org/urls/gist.github.com/ChrisBeaumont/5758381/raw/descriptor_writeup.ipynb
                   
Пользовательские атрибуты в Python
http://habrahabr.ru/post/137415/
                   
О порядке поиска пакетов и модулей для импорта в Python 
http://habrahabr.ru/post/166463/

Создание zip-модулей в python 
http://habrahabr.ru/company/acronis/blog/208378/

Python на колёсах
http://habrahabr.ru/post/210450/

Создание python-пакетов 
http://klen.github.io/create-python-packages.html
https://packaging.python.org/

Выкладка python-проектов с помощью pip и wheel 
http://habrahabr.ru/post/172219/

Облегчаем использование pyinstaller для создания exe  
http://habrahabr.ru/post/104589/

pyinstaller  
https://github.com/pyinstaller/pyinstaller/wiki

Как создавать пакеты
https://packaging.python.org/tutorials/distributing-packages/
"""
