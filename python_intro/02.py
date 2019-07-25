##  Встроенные типы

### Пустое значение
None

### Логические значения
True
False

bool(0)
bool(-1)
bool(None)

### Числа
# Целые
1
100_000
int('1')

# С плавающей запятой      
1.1
float('1.1')

# Особенности деления
# обычный вариант
7/3
# целочисленное деление
7//3
# остаток деления
7%3
# два в одном
divmod(7,3)

### Последовательности в Python

# Типы последовательностей: Изменяемые и не изменяемые

#### Строки
# https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

"строка", 'стр"о"ка', 'hello \n world'
print('hello\nworld')

# сырые строки
print(r'hello\nworld')

# Преобразование к строке
str(1)

#### Многострочные строки
"""
Hello
world
"""

# Строки это последовательность
'hello'[0]

#### Списки List
# https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range

l = [1, 2, 'string']

[1, [2, 'three'], 4]

#### Кортежи: Tuple
# неизменяемый тип данных
t = (1, 'spam', 4, 'U')

# Коварная запятая
a = 1
b = (1)
c = 1,
d =(1,)
print(type(a), type(b), type(c), type(d))

# Доступ к элементу
l[0]
t[0]

# Присвоение значение элементу
l[0] = 0
l

# Так нельзя. Кортеж неизменяем.
t[0] = 0

# Срезы: Считаются промежутки между элементами
l[1:2]

# Промежутки для списка
#  1 2 3
# ^ ^ ^ ^
# 0 1 2 3

# Взятие элементов в конце списка
l[-1]

# Дублирование списков и кортежей
'-' * 80

[0] * 10
l = [[]] * 3
l
l[0].append(1)
l

(1,2,3) * 3

# Генерация списка целых чисел
range(5)
range(3, 12, 3)

# Создание пустого списка 
empty_list = []

# Различные способы получения методов списка
dir(list)
dir([])
dir(empty_list)
help([])


#### Словари Dictonary
# https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

d = {'food': 'spam', 'taste': 'yum'}
d['food']

# Создание пустого словаря
d = {}

# методы словаря
dir(dict)
help({})


#### Множества Set
# https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset

set('abbc')
{'a', 'b', 'c'}

s1 = {1, 2, 3}
s2 = {3, 4, 5}

# Операции с множествами
# Пересечение
s1 & s2

# Объединение
s1 | s2

# Разность
s1 - s2
s2 - s1

# Надмножество
s1 > {1, 2}
s1 > {4, 5}

# методы множества
dir(set)


### Представления двоичных данных bytes, byte-array
# https://docs.python.org/3/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview

b'abc'
b'\x01\x02'
bytes('abc', 'ascii')
B = 'привет'.encode()
B
B.decode()

# bytearray изменяемая последовательность
B = bytearray('spam', 'latin1')
B[0] = ord('E')
B

### Файлы
myfile = open('lessons/02.py', 'r')
type(myfile)

## Сами типы
type(type)
type(object)


### Модули
import re
type(re)

### Операции над типами
dir(list)
help(list)

#### Динамическая типизация
# тип имеет не переменная, а ее содержимое
a = 1
type(a)
a = 'a'
type(a)

#### Разделяемые ссылки
a = 4200
b = a

# функция id: уникальный идетификатор объекта (его адрес)
id(a)
id(b)

# имя   ссылки   объекты
# a --->  42
# b ------^
a = 'spam'
# имя   ссылки   объекты
# a ---> 'spam'
# b --->  42
id(a)
id(b)

# Разделяемые ссылки и изменяемые объекты
L1 = [1, 2, 3]
L2 = L1
id(L2) == id(L1)
# имя   ссылки   объекты
#  L1 ---> [1, 2, 3]
#  L2 -----^

L1.append(4)
L1
L2
#  L1 ---> [1, 2, 3, 4]
#  L2 -----^

# копия списка
L2 = L1[:]
#  L1 ---> [1, 2, 3, 4]
#  L2 ---> [1, 2, 3, 4]
id(L2) == id(L1)
L2 is L1  # id(L2) == id(L1)
L1 == L2


## Синтаксис
### Структура программы на языке Python
# Модули -> инструкции -> выражения -> объекты

### Инструкции
a = 1
b = 2
print(a, b)

# Несколько специальных случаев
a = 1; b = 2; print(a, b)

### Присваивание
a = 1
b = 2
a, b = b, a
a, *b = 'good', 'bad', 'ugly'
print(a, ':', b)

### Длинные строки
# Обратный слеш в конце строки
very_very_very_long_variable_name = \
    2
# но лучше использовать скобки
very_very_very_long_variable_name2 = (
    2 + 2)

### Встроенные ключевые слова
# https://docs.python.org/3/reference/lexical_analysis.html#keywords
# import, def, class, if, while и др.

#### if
if a == 1 or b == 2:
    print(1)
elif a == 2:
    print(2)
else:
    print(3)

#### Трехместное выражение if/else
a = True
A = 'Y' if a else 'Z'
A

a = False
A = 'Y' if a else 'Z'
A

# Допустимо записывать одну инструкцию в нескольких строках
c = 1
d = 2
if (a == 1 and
    b == 2 and
    c == 3 and
    d == 4):  # Не забываем про двоеточие
    print('spam' * 3)

# Тело инструкции в одной строке
if a < b: print(c)


#### while, break, continue, pass, else
while a > 1:
    a = a - 1
    if a % 2:
        continue  # Перейти в начало циклa
    result = id(a)
    if result:
        break  # Выйти из цикла, пропустив часть else
else:  # Выполняется, если _не_ была использована инструкция 'break'
    print("bad action")

#### for
# полный вариант
for i in range(10):  # Присваивает элементы объекта с переменной цикла
    res = id(i)
    if res > 0: break  # Выход из цикла, минуя блок else
    if res < 0: continue  # Переход в начало цикла
else:
    print("good")  # Если не была вызвана инструкция 'break'

# простой вариант
for i in range(5,10,2):
    print(i)

### Приемы программирования циклов
#### Счетные циклы:  range
list(range(5))
list(range(10, 20))
list(range(5, 30, 7))
for i in range(3):
    print(i, ' Pythons')

#### Генерирование индексов и элементов: enumerate
S = 'spam'
for (offset, item) in enumerate(S):
    print(item, 'appears at offset', offset)

# Сортировка массива
origin = 'avdsdf'
sorted(origin)
#['a', 'd', 'd', 'f', 's', 'v']
origin

origin = [3, 1, 2]
origin.sort()
origin

# Удобный поиск подстроки
s = 'spam'
'm' in s
# Или элемента в массиве
1 in [0, 1, 2]


## Менеджер контекста
with open('lessons/02.py', encoding='utf8') as myfile:
    content = []
    for line in myfile:
        content.append(line)
    print(len(content))


## Итераторы
# Для унификации работы с последовательностями содан специальный протокол.
# Например все что используется в операторе 'for' справа от 'in' является итератором

I = [1, 2]
I = (1, 2)
I = {1, 2}
I = {"1": 1, "2": 2}

#работа с элементами  с помощью цикла
for l in I:
    print(l)

## Генерация последовательностей

# Создание списков в виде инструкции
L = [i for i in range(5)]
# то же самое в виде цикла
L = []
for i in range(5):
    L.apend(i)

# список нечетных чисел
L = [i for i in range(10) if i % 2]
# то же самое в виде цикла
L = []
for i in range(5):
    if i % 2:
        L.append(i)

# множество:
{i for i in range(5)}

# словарь:
{i: i + 1 for i in range(5)}

#с помощью цикла
d = {}
for i in range(5):
  d[i] = i + 1  

#Похоже на создание последовательностей в виде литералов
#сравните:
[0, 1, 2]
[i for i in range(3)]

{0, 1, 2}
{i for i in range(3)}

{0:1, 1:2, 2:3}
{i: i + 1 for i in range(3)}

# Выражения-генераторы реализация "ленивых" вычислений
(i for i in range(5))

"""
Материал для дополнительного изучения:

Python: коллекции
https://habrahabr.ru/post/319164/
https://habrahabr.ru/post/319200/
https://habrahabr.ru/post/319876/
https://habr.com/en/post/320288/
"""