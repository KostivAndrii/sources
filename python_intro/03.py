## Ввод/вывод

### Ввод текста в консоли
type(i)

# Использование текста
print(i, int(i)*2)

### Форматированый вывод
# примеры: безномерной, номерной именованый
i = 1
"I have " + str(i) + " apple"

"I have {} apples and {} bananas".format(3, 2)
"I have {1} apples and {0} bananas".format(3, 2)
"I have {apple} apples and {banan} bananas".format(apple=3, banan=2)

# Полный синтаксис
# https://docs.python.org/3/library/string.html#formatspec

# Начиная с версии 3.6 доступен новый синтаксис
# Форматирование в виде литералов:
f"I have {i} apple."

# Где найти еще примеры
# https://docs.python.org/3/library/string.html#string.Template.template
#string.Template.template

# Старый вариант с использованием процента
"I have %i apples" % 2

### Использование функции print
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
print(1,2,3)
print(1,2,3, sep=';')
print(1,2,3, sep='-', end=';')
print()

# Все строки в юникоде
# Кодировка входных файлов разная
# Строки можно кодировать
"abc абв".encode('cp1251')

# и обратно
b'abc \xe0\xe1\xe2'.decode('cp1251')
# 'abc абв'

### Открытие файла
# текстовые файлы:
# open() открывает файл и возвращает "файл-подобный" объект
f = open("lessons/examples/fox.txt")
type(f)

### Открытие файла с кодировкой
# Можно указать кодировку при чтении/записи в текстовом режиме
f = open("lessons/examples/citrus-1251.txt", encoding="cp1251")
# чтение строки
f.readline()
# чтение всего файла в одну строку
f.read()
f.seek(0)
# чтение в список
f.readlines()

# закрытие файла, когда он больше не нужен
f.close()

f = open("lessons/examples/citrus-utf8.txt", encoding="utf8")
f.readline()
f.close()

# работа с каждой строкой
for line in open("lessons/examples/fox.txt"):
   print(line.strip())

# запись в файл
f = open("test.txt", "w")  # "w" - создать файл для записи
f.write("Тест\n")              # записать в file-подобный объект
f.write("проверка")

# печать в файл
print("text", file=f)
f.close()

# менеджер контекста
with open('spam.txt', 'w') as file:
    file.write('Spam and eggs!')

# загрузка из бинарного файла
fb = open("lessons/examples/citrus-1251.txt", "rb")
citrus=fb.read()
print(citrus.decode(encoding='cp1251'))
fb.close()


fb = open("testw.txt", "wb")
fb.write(b'hello')
fb.write("Привет".encode("cp1251"))
fb.close()


## Функции

# Определение функции
### Документирование
def fun1(arg1, arg2):
    "Documentation"
    print(arg1, arg2)

fun1('hello', 'world')

# Начиная с версии 3.5 можно опциально описывать типы
# входящих данных и тип возвращаемого значения
def fun_with_types(i: int, s:str) -> bool:
    return s[i] == 'a'


fun_with_types(1, "ddd")
   
# Но все так же можно передавать любые типы
fun_with_types(1, ['a','a'])

# Для статической проверки типов используется пакет mypy


### Переменное количество аргументов
def fun2(x, y, *args, **kwargs):
    print(x,y, args, kwargs)
    if args:
        print("args[0]: {}".format(args[0]))
    if kwargs:
        print("kwargs['parameter']: {}".format(kwargs.get('parameter')))

fun2(1, 2)
fun2(1, 2, 3 ,4)
fun2(1, 2, 3 ,4, parameter=1)
fun2(1, 2, 3 ,4, param=1)

### Значения по умолчанию
def fun3(a, d=1):
    print(a, d)

fun3(1)
fun3(1, 2)

### Именованные параметры
fun3(a=3, d=4)

### Упаковка и распаковка параметров
# *args
# **kwargs
def fun4(a, *args):
    print(a, args)
    if args:
        print("args[0]: {}".format(args[0]))

l = [1,2,3]

### Распаковка списка при вызове функций
fun4(1, 2, *l)
fun4(1, 2, l)
fun4(1, 2, 1, 2, 3)


def fun5(a, b, c):
    print(a, b, c)

fun5(*l)

### Возвращаемое значение по умолчанию
def default():
    pass

print(default())

### Возвращение нескольких значений
def mulret():
    return 1, 2, 3

print(mulret())
a, b, c = mulret()
print(a, b, c)
### Замыкания
def outer(a):
        def inner(c):
                return a + c
        return inner

closure = outer(1)
closure
print(closure(2))


# Расширенные функции
### lambda
lambda x, y: x + y + 1
adder = lambda x: x + 1
adder(2)

# допускается создание идентификаторов на русском языке, но лучше так не делать.
список = [(1, 3), (2, 2), (3, 1)]
sorted(список, key=lambda i: i[1])

### Встроенные функции
# https://docs.python.org/3/library/functions.html?highlight=builtin%20functions

min(1, 2)
max([1, 4, 6, 3])

#### Параллельный обход: zip
L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]
zip(L1, L2)
list(zip(L1, L2))
dict(zip(L1, L2))

for x, y in zip(L1, L2):
    print(x, '+', y, '=', x + y)

### Функциональные инструменты
#### Генераторы списков и функция map
help(ord)
m = map(ord, 'spam')
list(m)
L = 'spam'
[ord(i) for i in L]

#### Функция filter
L = [1, 0, None, True, 2]
list(filter(bool, L))
[i for i in L if i]


#### Функция any
L = [True, None, 1]
any(L)

#### Функция all
all(L)


### Функции высшего порядка
# map, filter
map(lambda x: x*x, [1, 2, 3, 4, 5])
l = [1, 2, 3, 4, 5]
list(filter(lambda x: x%2, l))


def superfun(fun, arg1, arg2):
        return fun(arg1, arg2)

superfun(min, 1, 2)
superfun(max, 1, 2)


## Области видимости
#
# LEGB Rule.
# L. Local.
# E. Enclosing function locals.
# G. Global (module)
# B. Built-in (Python)
# вложеные функции
x = 1
def outer(a):
        b = 2
        def inner(c):
                d = 3
                print("a=", a)
                print("b=", b)
                print("c=", c)
                print("d=", d)
                print("x=", x)
        return inner

i = outer(5)
i(6)

### Инструкция global
def fun_not_global():
        x = 2

def fun_global():
        global x
        x = 2

x = 1
print(x)
fun_not_global()
print(x)
fun_global()
print(x)

### nonlocal
b=2
def outer(a):
        b = 1
        def inner(c):
                nonlocal b
                b = 2
        inner(5)


### Изменяемые аргументы как параметры функций
def f1(l: list):
    l.append(3)

def f2(l):
    l = [3]

arg = [2]
f1(arg)
print(arg)
f2(arg)
print(arg)

arg = 1
# Генерируется ошибка т.к. несовместимый параметр
f1(arg)


### Область видимости для изменяемых значений
# Это работает
x = 10
def bar():
    print(x)
bar()

# это выдает исключение
x = 10
def foo():
    print(x)
    x = x + 1
foo()

# исправление ситуации
x = 10
def foobar():
    global x
    print(x)
    x = x + 1
foobar()
"""
Материал для дополнительного изучения:

Как сделать функции на Python еще лучше 
https://habr.com/en/company/piter/blog/426381/
"""