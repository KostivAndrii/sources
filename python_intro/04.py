## Классы и ООП

### Основы: создание класса
class First:
    "Определяет объект класса"
    cl = 1 # переменные для всех экземпляров класса

    def __init__(self, value): # конструктор
        # self – это экземпляр
        self.data = value
        self._v1 = None

    def _setdata(self, value): # Определяет метод класса
        self.data = value

    def display(self):
        print(self.data, self._v1)

#Сам класс является объектом
type(First)

# атрибуты экземпляра и класса
f1 = First(1)
f2 = First(2)

f1.data
f2.data

f1.cl
f2.cl


# Изменять атрибут класса можно только из объекта класса
First.cl = 3
f1.cl
f2.cl

f1.cl = 2
f1.cl
f2.cl


# Вызов метода
f1.display()

### Наследование и функция super()
class Second(First):
    def __init__(self, value, me):
        self.me = me
        # Необходимо вызывать вручную если переопределили конструктор
        super().__init__(value)
        print(super())

    def display(self):
        super().display()
        print("I am second {}".format(self.data))

    @staticmethod
    def stat():
        print('static')

s1 = Second(3, 'class')
s1.me
s1.display()
s1.stat()

type(s1)
type(Second)

# Базовые классы
Second.__bases__

# Пример ромбовидного наследования
#   Base
#  D1  D2
#    C1

class Base:
    pass

class D1(Base):
    pass

class D2(Base):
    pass

class C1(D1, D2):
    pass

class C2(D2, D1):
    pass

# Порядок поиска определяется алгоритмом С3.
# Порядок поиска можно найти в переменной __mro__
C1.__mro__
C2.__mro__
# Функция super() ищет базовые классы с помощью этой переменной


# специальные методы __init__() вызываются автоматически
# например __str__()
class Third(First):
    def __repr__(self):
        return '__repr__: <ThirdClass: {}>'.format(self.data)

    def __str__(self):
        return '__str__: [ThirdClass: {}]'.format(self.data)

t1 = Third(2)
t1
t1.data=2
print(t1)

### Внутренние атрибуты классов и экземляров

class Noop:
    """I do nothing at all."""



Noop.__doc__
Noop.__class__
Noop.__name__
Noop.__module__
Noop.__bases__

noop = Noop()

noop.__class__
noop.__dict__
noop.name = 'Bob'
noop.__dict__


### Перезагрузка операторов
# Магические методы
# __getattr__
# __eq__
# __lt__
# __add__
# __call__
# __repr__
# Полный список https://docs.python.org/3/reference/datamodel.html#special-method-names

class Magic:
    def __init__(self, value): # конструктор
        # self – это экземпляр
        self.data = value
    def __add__(self, other):
        return self.data + other.data

m1 = Magic(1)
m2 = Magic(2)
m1 + m2
m1.__add__(m2)
m1.data

# функция getattr, setattr, delattr
getattr(m1, "data")
getattr(m1, "unknown", None)
setattr(m1, "data", 100)


### Объектная система языка
type(m1)
type(Magic)
type(type(Magic))

# Экземпляры 'типа type' или 'класса object' — это объекты (любые).
# Т.е. любой объект — экземпляр класса object:
help(isinstance)
isinstance(1, object)
isinstance(setattr, object)
isinstance("foo", object)
isinstance(Magic, object)
isinstance(type, object)

# Даже функция является объектом:
def bar():
    pass

isinstance(bar, object)
isinstance(First.display, object)


# Кроме того, класс object сам является своим экземпляром:
isinstance(object, object)

# Экземпляры 'класса' или 'типа type' — это только другие классы или другие типы:
# Число — это не класс
isinstance(1, type)

# Строка тоже
isinstance("foo", type)

# Класс — это класс.
isinstance(Magic, type)
isinstance(Second, type)
isinstance(type, type)
isinstance(object, type)


### Реализация менеджера контекста в виде класса
# ключевое слово with
# менеджер контекста
with open('filename') as openfile:
    pass

class File():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, type, value, traceback):
        self.open_file.close()

with File('lessons/foo.txt', 'w') as infile:
    infile.write('foo')

### Метод __new__ для класса
class Singleton():
    s = None
    def __new__(cls):
        if Singleton.s:
            print('use', Singleton.s)
            return Singleton.s
        else:
            Singleton.s = super(Singleton, cls).__new__(cls)
            print('created object', Singleton.s)
            return Singleton.s

    def __init__(self):
        print('init ', self)


single = Singleton()
id(single)
single = Singleton()
id(single)


### Метаклассы
# Классы - создающие классы (т.е. новые типы)

# Все классы в Python — это экземпляры класса type.
class Something:
    attr = 42

Something
type(Something)


# класс type называют метаклассом, то есть классом, экземпляры которого тоже классы.
# Экземпляры класса или типа type — это только другие классы или другие типы.

name, bases, attrs = "Something", (), {"attr": 42}
Something = type(name, bases, attrs)
Something
some = Something()
some.attr


### Эмуляция интерфейсов
class Interface():
    def f1(self):
        raise NotImplemented()

    def f2(self):
        pass


class Action(Interface):
    def f1(self):
        print("Hello")

i = Interface()
i.f1()
i.f2()
a = Action()
a.f1()
a.f2()

#### Стандартный базовый класс
# https://docs.python.org/3/library/index.html
from abc import ABCMeta, abstractmethod, abstractproperty
class Movable(metaclass=ABCMeta):
    @abstractmethod
    def move():
        "Переместить объект"

    @property
    @abstractmethod
    def speed():
        "Скорость объекта"

m = Movable()

class Car(Movable):
    def __init__(self):
        self.speed = 10
        self.x = 0

    def move(self):
        self.x += self.speed

    def speed(self):
        return self.speed


c = Car()
c.move()
c.speed

issubclass(Car, Movable)
isinstance(Car(), Movable)


### Утинная типизация
# Название термина пошло от английского «duck test» («утиный тест»), который в оригинале звучит как:
#  Если это выглядит как утка, плавает как утка и крякает как утка, то это, вероятно, и есть утка.

# Если объект реализует все методы какого-то интерфейса,  то говорят, что он реализует этот интерфейс.


## Исключения

### Назначение исключений
#  - Обработка ошибок
#  - Уведомления о событиях
#  - Обработка особых ситуаций
#  - Заключительные операции

### Использование исключений

try:
#    raise SyntaxError("My syntax error")
    Nones # NameError
#    1 + "2" # TypeError
#    [1,2][3] # IndexError
    print("All fine")
except NameError:
    print("Name error.")
except IndexError as ie:
    print("Index error:", ie)
except (AttributeError , TypeError) as e:
    print("AttributeError or TypeError!!!")
else: # Выполняется, если не было исключений.
    print ("In else block")
finally: # Этот блок выполняется всегда.
    print ("In finally block")

### Объекты исключений
# Исключение без параметров
# Обязательное наследование от Exception

class Simple(Exception):
    def __str__(self):
        return "I am simple exception"

try:
    raise Simple
    #raise Simple() # можно вызвать и так
except Simple as s:
    print("Simple error: ", s)

# Исключение с параметром
class General(Exception):
    def __init__(self, v):
        self.v = v

    def __str__(self):
        return "I am general exception {}".format(self.v)

try:
    raise General('bad')
except General as e:
    print("Oh no!!! General error!!! -> {}".format(e))
except Exception as e:
    print(e)


### Программная генерация исключения assert
try:
    assert 1 > 2, "Error"
except AssertionError as g:
    print("Assett error: ", g)
    raise

# Стандартные исключени и иерархия классов
# Стандартные исключения
# https://docs.python.org/3/library/exceptions.html

# Иерархия стандартных исключений
# https://docs.python.org/3/library/exceptions.html#exception-hierarchy

"""
Материал для дополнительного изучения:

Python types and objects 
объяснение объектной модели python на простых примерах 
https://habrahabr.ru/post/114576/
https://habrahabr.ru/post/114585/
https://habrahabr.ru/post/114587/

A Guide to Python's Magic Methods 
https://rszalski.github.io/magicmethods/

Паттерн проектирования «Команда» / «Command» 
http://habrahabr.ru/post/114455/

Порядок разрешения методов в Python
https://habrahabr.ru/post/62203

Использование исключений
https://doughellmann.com/blog/2009/06/19/python-exception-handling-techniques/
"""