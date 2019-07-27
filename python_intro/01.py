## Начало работы

### Запуск интерпретатора
"""
Windows
> python

Linux
> python  - Python 2.x
> python3 - Python 3.x
"""

### Виртуальные окружения
"""
создание окружения
> python -m venv venv_dir

активация окружения
Windows
> venv_dir\bin\activate.bat

Linux
> source venv_dir/bin/activate
"""


### Пакетный менеджер pip

# Основной репозиторий: pypi.org
"""
Windows
> pip

Linux
> pip - Python 2.x
> pip3 - Python 3.x

Запуск через интепретатор (полезно для запуса pip из виртуального окружения)
python -m pip 

Установка пакета из pypi.org
pip install ProjectName

Установка пакета из архива с локального диска
pip install ./dist/ProjectName.tar.gz

Установка пакета из каталога. В каталоге должен находится файл setup.py.
pip install ./dist/ProjectName

Установка пакета из каталога в режиме разработчика. В каталоге должен находится файл setup.py.
pip install -e ./dist/ProjectName


Установка пакета из git репозитория
pip install git+https://gitrepo.com/ProjectName.git
pip install https://gitrepo.com/ProjectName/archive/master.zip

Удаление пакета
pip uninstall ProjectName
"""


## Функции помощи

# Дзен питона
import this

### Встроенная помощь: функция help
help(help)

# Все есть объекты
### Список методов класса: функция dir
dir(int)
dir(1)

i=1025
i.bit_length()

### Узнать тип объекта: функция type
type(1)
type('hello')
type(type)


# Простой пример программы
n = 10
a = 0
b = 1
f = [a]
for i in range(n):
    temp = a
    a = b
    b += temp
    f.append(a)
print("Fibonacci number for {} is {}".format(n, a))

# Создание диаграммы

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(len(f))
plt.bar(x, height= f)


# Использование стандартных библиотек библиотек
# https://docs.python.org/3/library/turtle.html
import turtle
for _ in range(4):
    turtle.forward(100)
    turtle.left(90)


# Проекто Jypiter
# http://jupyter.org/
# https://try.jupyter.org/
# 01notebook.ipynb
# jupyter notebook

# Cервис от Google
# https://colab.research.google.com/

"""
Материал для дополнительного изучения:

PyPi
https://pypi.org/

Установка пакетов с помощью pip
https://python-packaging-user-guide.readthedocs.io/tutorials/installing-packages/

Зачем изучать питон
http://habrahabr.ru/post/150302/

Отличие 2 от 3 версии
https://wiki.python.org/moin/Python2orPython3

Гвидо ван Россум отвечает на вопросы
http://habrahabr.ru/post/196624/


Дзен питона
http://www.russianlutheran.org/python/zen/zen.html

IPython: замена стандартного Python shell
http://habrahabr.ru/post/49685/

The Hitchhiker’s Guide to Python!
https://docs.python-guide.org/

* Литература
Swaroop Chitlur. A Byte of Python 
    английский вариант: https://python.swaroopch.com/
    перевод на русский: http://wombat.org.ua/AByteOfPython/
Марк Лутц. Изучаем Python, 4-е издание 1200с.
Марк Лутц. Программирование на Python
Марк Саммерфилд. Программирование на Python 3. Подробное руководство
Лучано Рамальо. Python. К вершинам мастерства
"""