## Идиоматика Python

# Пиши код, как настоящий Питонист: идиоматика Python

### Проверка истиности для множеств
# if x:
# if not x:
# GOOD
name = 'Safe'
pets = ['Dog', 'Cat', 'Hamster']
owners = {'Safe': 'Cat', 'George': 'Dog'}
if name and pets and owners:
    print('We have pets!')

# NOT SO GOOD
if name != '' and len(pets) > 0 and owners != {}:
    print('We have pets!')

bool({})
bool({1:2})


###  Использовать выражение "in": if x in items
# GOOD
name = 'Safe Hammad'
if 'H' in name:
    print('This name has an H in it!')

# NOT SO GOOD
name = 'Safe Hammad'
if name.find('H') != -1:
    print('This name has an H in it!')

## for x in items
# GOOD
pets = ['Dog', 'Cat', 'Hamster']
for pet in pets:
    print('A', pet, 'can be very cute!')

# NOT SO GOOD
pets = ['Dog', 'Cat', 'Hamster']
i = 0
while i < len(pets):
    print('A', pets[i], 'can be very cute!')
    i += 1

### Обмен значениями двух переменных
a = 1
b = 2
a, b = b, a
print(a, b)

### Объединение списков в строку: ''.join(some_strings)
# GOOD
chars = ['This', 'is', 'the', 'webinar']
name = ' '.join(chars)
print(name) # Safe

# NOT SO GOOD
chars = ['S', 'a', 'f', 'e']
name = ''
for char in chars:
    name += char
print(name) # Safe

### Использовать enumerate
# for i, item in enumerate(items):
# GOOD
names = ['Safe', 'George', 'Mildred']
for i, name in enumerate(names):
    print(i, name) # 0 Safe, 1 George etc.

# NOT SO GOOD
names = ['Safe', 'George', 'Mildred']
count = 0
for name in names:
    print(i, name) # 0 Safe, 1 George etc.
    count += 1

### Использовать генераторы списков
# GOOD
data = [7, 20, 3, 15, 11]
result = [i * 3 for i in data if i > 10]
print(result) # [60, 45, 33]

# NOT SO GOOD (MOST OF THE TIME)
data = [7, 20, 3, 15, 11]
result = []
for i in data:
    if i > 10:
        result.append(i * 3)
print(result) # [60, 45, 33]

### Создание словарей c помощью zip
# dict(zip(keys, values))
# GOOD
keys =   ['Safe',   'Bob',     'Thomas']
values = ['Hammad', 'Builder', 'Engine']
d = dict(zip(keys, values))
print(d) # {'Bob': 'Builder', 'Safe': 'Hammad', 'Thomas': 'Engine'}

# NOT SO GOOD
keys = ['Safe', 'Bob', 'Thomas']
values = ['Hammad', 'Builder', 'Engine']
d = {}
for i, key in enumerate(keys):
    d[key] = values[i]
print(d) # {'Bob': 'Builder', 'Safe': 'Hammad', 'Thomas': 'Engine'}

### Использовать _ для отбрасываемых переменных
for k, _ in [('a', 1), ('b', 2), ('c', 3)]:
    print(k)

### Использовать dict.get() and dict.setdefault()
d = {"a": 1, "b": 2}
d.get("a")
d.get("c", 2)
d["c"] # KeyError: 'c'
d.setdefault("c", 3)
d["c"]

### Сортировка списков
l = [3, 1, 2]
#с использованием функции: создание нового сортированного списка
sorted(l)
#метод объекта sort: сортировка на месте
l.sort()
l

l=[(1,3), (2,2), (3,1)]
l.sort(key=lambda x: x[1])
l
# В качестве параметра key любая функция принимающая одну перменную


### Инверсия порядка элеметов в списке
l = [3, 2, 1]
reversed(l)
l
l.reverse()
l


### Использование функций вместо класса с одним методом
class Dump:
    def __init__(self, var):
        self.var = var
    def action(self):
        print(self.var)

def dump(var):
    def action():
        print(var)
    return action

d = Dump(1)
d.action()

d = dump(2)
d()

### Пользовательские типы данных
# https://docs.python.org/3/library/collections.html
import collections
#collections.namedtuple
Point = collections.namedtuple('Point', ['x', 'y'])
p1 = Point(x=1, y=2)
p2 = Point(11, 22)
p1.x + p2.x

# collections.Counter
c = collections.Counter('gallahad')
c
c.update('aaa')
c


### Модуль itertools
# https://docs.python.org/3/library/itertools.html
from itertools import *
c = 0
for i in cycle('ABCD'):
    print(i, end=' ')
    if c == 10:
        break
    c += 1
else:
    print('No break') # Этот код не будет выполнет
print("\nc =", c)

# Счетчик лучше включать в последовательность с помощью enumerate(cycle('ABCD'))
for i in repeat(10, 3):
    print(i)


### Документирование кода
# docstring
def add1(v):
    """This is very useless  function.
    @v: int - just variable
    @:return int
    """
    return v + 1

help(add1)

# Sphinx генерация документации для питона
# https://pypi.org/project/Sphinx/

# pdoc
# pydoc


## Практические возможности

### Профилирование и отладка
# https://docs.python.org/3/library/time.html
import time
start = time.time()
time.sleep(3)
# или какой-то нужный код
done = time.time()
elapsed = done - start
print(elapsed)

#### timeit
# https://docs.python.org/3/library/timeit.html
import timeit
t1 = timeit.Timer("text='sample string'; char = 'g'; char in text")
t1.timeit()
def s(text, char):
    for c in text:
        if c == char:
            return True
    return False
t2 = timeit.Timer("s('sample string', 'g')", setup='from __main__ import s')
t2.timeit()

# есть интерфейс командной строки
# python -m timeit -s "text = \"sample string\"; char = \"g\""  "char in text"
# python -m timeit -s "text = \"sample string\"; char = \"g\""  "text.find(char)"


#### profile
# https://docs.python.org/3/library/profile.html
import cProfile
import re
cProfile.run('re.compile("foo|bar")')

#### Отладчик pdb
# https://docs.python.org/3/library/pdb.html
import pdb
pdb.set_trace()

# import pdb; pdb.set_trace()
# интерактивная отладка

# Начиная с версии 3.7 можно использовать новую функцию
# breakpoint()

#### Отладчик ipdb
# pip install ipdb
# import ipdb; ipdb.set_trace()


#### Отладчик pudb
#PuDB is a full-screen, console-based visual debugger for Python.
# pip install pudb
# import pudb; pudb.set_trace()

### Тестирование кода
# https://docs.python.org/3/library/unittest.html
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FO1O')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

# Пример файла examples/test.py
# документация модуля unittest

#### unittest.mock
# https://docs.python.org/3/library/unittest.mock.html
from unittest.mock import MagicMock
class ProductionClass():
    def method(self):
        pass
thing = ProductionClass()
thing.method = MagicMock(return_value=3)
thing.method(3, 4, 5, key='value')
thing.method.assert_called_with(3, 4, 5, key='value')

#### patch
with unittest.mock.patch.object(ProductionClass, 'method', return_value=None) as mock_method:
    thing = ProductionClass()
    thing.method(1, 2, 3)

mock_method.assert_called_once_with(1, 2, 3)
# Вызов исключения если вызвано с другими параметрами
mock_method.assert_called_once_with(1, 2, 4)

#### pytest - простое создание тестов
# https://pypi.org/project/pytest/
# nose - более мощное средство, больше возможностей
# https://pypi.org/project/nose/

# Возможности pytest
#Создание тестов вне специального класса
def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 5

# Запуск всех тестов в каталоге
# $ pytest

# Запуск определенного теста
# $ pytest test_mod.py::TestClass::test_method

# Порядок запуска тестов
@pytest.mark.run(order=2)
def test_foo():
    assert True

@pytest.mark.run(order=1)
def test_bar():
    assert True

# Расширенные фикстуы
@pytest.fixture(scope="function", params=[
    ("abcdefg", "abcdefg?"),
    ("abc", "abc!"),
    ("abcde", "abcde.")])
def param_test(request):
    return request.param


def test_strange_string_func(param_test):
    (input, expected_output) = param_test
    pass


### tox - тестирование с помощью virtualenv
# https://pypi.org/project/tox/


### Selenium
# https://pypi.org/project/selenium/
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        assert "No results found." not in driver.page_source
        elem.send_keys(Keys.RETURN)

    def tearDown(self):
        self.driver.close()


### Генерация тестовых данных
# faker
# https://pypi.org/project/faker/
# testdata
# https://pypi.org/project/testdata/


### Статическая проверка кода
# flake8
# https://pypi.org/project/flake8/
# pylint
# https://pypi.org/project/pylint/


### Программирование GUI
# https://docs.python.org/3/library/tkinter.html
from tkinter import *
from tkinter.messagebox import showinfo
def reply():
    showinfo(title='popup', message='Button pressed!')
window = Tk()
button = Button(window, text='press', command=reply)
button.pack()
window.mainloop()
# Пример в файле lessons/examples/gui.py

### Работа с внешними библиотеками
# https://docs.python.org/3/library/ctypes.html
from ctypes import *
# windows
print(windll.kernel32)
print(windll.kernel32.GetModuleHandleA)
# linux
libc = CDLL("libc.so.6")
libc
libc.printf


### Работа с COM объектами
#pip install pywin32
import win32com.client
from collections import Counter
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)  # "6" is Inbox
messages = inbox.Items
message = messages.GetFirst()
name = getattr(message, "SenderName", "NoName")

### Системные инструменты

#### paramiko - SSH client
# https://pypi.org/project/paramiko/
# https://github.com/axper/python3-pycrypto-windows-installer

#### fabric3
# https://pypi.org/project/Fabric3/
# pip install fabric3
#fabfile.py:
# ------------------------
from fabric.api import run

def host_type():
    # запуск на удаленной машине через ssh
    run('uname -s')

def hello():
    print("Hello world!")
# ------------------------
#fab -l
#fab hello
#fab host_type

with settings(host_string='12.34.56.78', user='user', password='pass'):
    run("hostname -f")

local("dir")

#### subprocess
# https://docs.python.org/3/library/subprocess.html
import subprocess
subprocess.run(["notepad"]) # windows
subprocess.run(["leafpad"]) # linux
output = subprocess.run(["ipconfig"], stdout=subprocess.PIPE) # windows
output = subprocess.run(["ifconfig"], stdout=subprocess.PIPE) # linux
print(output.stdout.decode())


### Параметры командной строки
import sys
sys.argv

#### argparse
# https://docs.python.org/3/library/argparse.html
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                   help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                   const=sum, default=max,
                   help='sum the integers (default: find the max)')

args = parser.parse_args()

#### click
# pip install click
# https://pypi.org/project/click/
import click
@click.command()
@click.option('--test', default="DEFAULT_CONFIG",
              help='Test case ')
@click.option('--config', default="DEFAULT_TESTER",
              help='Test configuration file.')
def run(test, config):
    print(test, config)

### Логирование
# logging
# https://docs.python.org/3/library/logging.html
import logging
# настройка корневого логгера
# отправка сообщений stderr
logging.basicConfig(level=logging.INFO)
# отправка сообщений в stdout
import sys
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
# отправка сообщений в файл
logging.basicConfig(filename="info.log", level=logging.DEBUG)
logging.warning("My message")

# Создание пользовательского логгера
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.info('I told you info')
logger.error('I told you error')

# Более гибкая настройка логгера с помощью handler и formatter
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)

logger.parent
logger.name

# Пример имени "foo.bar.my_module"
# логгеры создают иерархию соответсвующую имени модуля
# Иерархия начинается с с логера 'root'.
# Если для логера не определены настройки, они берутся из
# родительского логера


## Библиотека loguru
# альтернатива стандартному logging
# https://github.com/Delgan/loguru


### Обработка форматированных данных
### html
#html.parser
#https://docs.python.org/3/library/html.parser.html#module-html.parser

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)

parser = MyHTMLParser()
parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')

#### xml
# xml.etree.ElementTree
# https://docs.python.org/3/library/xml.etree.elementtree.html
import xml.etree.ElementTree as ET
tree = ET.parse('lessons/examples/country_data.xml')
root = tree.getroot()
root.tag
root.attrib
for child in root:
   print(child.tag, child.attrib)

# lxml
# https://pypi.org/project/lxml/


# Универсальный парсер
# beautifulsoup4
# https://pypi.org/project/beautifulsoup4/

#### cvs
# https://docs.python.org/3/library/csv.html
import csv
import sys
csvfile=sys.stdout
spamwriter = csv.writer(csvfile, delimiter=',',
                        quotechar='"')
with open('lessons/examples/eggs.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|', skipinitialspace=True)
    for row in spamreader:
        spamwriter.writerow(row)

#### json
# https://docs.python.org/3/library/json.html
import json
data = json.loads(open("lessons/examples/test.json").read())
print(json.dumps(data, indent=2))

#### yaml
# pip install pyaml
# pyaml
# https://pypi.org/project/pyaml/
import sys
import yaml
data = yaml.load(open("lessons/examples/test.yaml"))
yaml.safe_dump(data, sys.stdout)

#### Модуль struct загрузка структурированных данных
# https://docs.python.org/3/library/struct.html
import struct
#экспорт данных
buf = struct.pack("IH", 1, 2)
buf
struct.unpack("IH", buf)


### Графики и диаграммы matplotlib
#https://pypi.org/project/matplotlib/

### Матричные вычисления, линейная алгебра: numpy
# https://pypi.org/project/numpy/

### Статистика, анализ данных: pandas
# (похожий функционал языка R)
# https://pypi.org/project/pandas/

#Wes McKinney "Python Data Analysys"

"""
Материал для дополнительного изучения:

Галерея лучших блокнотов по ML и Data Science 
https://habr.com/ru/post/460321/

идиомы питона 
http://habrahabr.ru/post/88972/
http://habrahabr.ru/post/89735/
http://habrahabr.ru/post/90493/
https://python-3-patterns-idioms-test.readthedocs.io/en/latest/

Профилирование и отладка Python 
http://habrahabr.ru/company/mailru/blog/201594/
http://habrahabr.ru/company/mailru/blog/201778/
http://habrahabr.ru/company/mailru/blog/202832/

Python Cookbook,Recipes for Mastering Python 3. By Brian Jones, David Beazley 
https://github.com/borisuvarov/python-cookbook-ru

#Testing Python Applications with Pytest
https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest

Путеводитель по Python. Пишем великолепный код 
http://habrahabr.ru/post/183912/

Python: советы, уловки, хаки 
http://habrahabr.ru/post/85238/
http://habrahabr.ru/post/85459/
http://habrahabr.ru/post/86706/ 
http://habrahabr.ru/post/95721/

Некоторые возможности Python о которых вы возможно не знали 
http://habrahabr.ru/post/196382/

Вещи, о которых следует помнить, программируя на Python 
http://habrahabr.ru/post/144614/

Python: вещи, которых вы могли не знать 
http://habrahabr.ru/post/207988/

Перестаньте писать классы
https://habrahabr.ru/post/140581/

Pytest
https://habrahabr.ru/post/269759/
https://habr.com/ru/post/448798/

Знакомство с тестированием в Python
https://habr.com/ru/company/otus/blog/433358/
https://habr.com/ru/company/otus/blog/433572/
https://habr.com/ru/company/otus/blog/444204/

Скрипты Python против Bash 
http://habrahabr.ru/post/47474/ 
http://habrahabr.ru/post/62383/

Работа с ssh в Python
http://habrahabr.ru/post/150047/

Python для системных администраторов 
http://habrahabr.ru/post/59419/

Logging — библиотека для удобного ведения логов в Python 
http://habrahabr.ru/post/144566/

Написание приложений, основаных на Qt, на языке Python 
http://habrahabr.ru/post/31426/

Интеграция MS Excel и Python 
http://habrahabr.ru/post/232291/

Интересные особенности Python, о которых вы могли не догадываться
https://habrahabr.ru/post/322360/

Module of the week:
https://pymotw.com/3/

5 распространенных ошибок начинающих программистов на Python
https://habr.com/ru/post/458902/
"""
