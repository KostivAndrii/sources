## Базы данных

### Реляцимонные базы

#### sqlite3
# https://docs.python.org/3/library/sqlite3.html
import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
conn.commit()
conn.close()

#### Mysql
# MySQL-python
# https://sourceforge.net/projects/mysql-python/

#### Postgresql
# psycopg2
# http://initd.org/psycopg/docs/


#### Python ORM
# SqlAlchemy
# https://pypi.org/project/SQLAlchemy/
# см. examples/mysqlalchemy.py

# Миграции БД
# Экспорт/импорт структуры базы Alembic
# alembic
# https://bitbucket.org/zzzeek/alembic


### NoSQL базы

#### redis
# redis-py
# https://github.com/andymccurdy/redis-py

import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)
r.set('foo', 'bar')
r.get('foo')

# см. examples/redispubsub.py


#### MongoDB
# pymongo
# https://github.com/mongodb/mongo-python-driver
# http://api.mongodb.com/python/current/tutorial.html
from pymongo import MongoClient
import datetime
client = MongoClient('localhost', 27017)
db = client.test_database
collection = db.test_collection
post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

posts = db.posts
post_id = posts.insert_one(post).inserted_id
db.collection_names(include_system_collections=False)
print(posts.find_one())



## Асинхронное и многопоточное программирование

### Генераторы с помощью yield

def countdown(n):
    print("Обратный отсчет!")
    while n > 0:
        print(n)
        yield n  # Возвращает значение (n)
        n -= 1

c = countdown(5)
next(c)
next(c)

for i in countdown(5):
     print(i)

### Сопродцедуры (corouting)
def typer():
    print("Обратный отсчет!")
    while True:
        n = yield
        print(type(n))

c = typer()
# Инициализация
next(c)

c.send(1)
c.send("Hello")


### Организация многопоточности

#### Threading
# ограничения: выполняется только 1 поток!
# https://docs.python.org/3/library/threading.html
import threading
import time

def clock(interval):
    while True:
        print("Текущее время: {}".format(time.ctime()))
        time.sleep(interval)

t = threading.Thread(target=clock, args=(1,))
t.daemon = True
t.start()

# С помощью класса
import threading
import time

class ClockThread(threading.Thread):
    def __init__(self,interval):
        threading.Thread.__init__(self)
        self.daemon = True
        self.interval = interval
    def run(self):
        while True:
            print("Текущее время: {}".format(time.ctime()))
            time.sleep(self.interval)

t = ClockThread(1)
t.start()

#### multiprocessing
# https://docs.python.org/3/library/multiprocessing.html
# запускаются в отдельном интерпретаторе
from multiprocessing import Process

#### Очереди
# https://docs.python.org/3/library/queue.html
import queue
import threading
def worker():
    while True:
        item = q.get()
        if item is None:
            break
        print(item)
        q.task_done()

q = queue.Queue()
num_worker_threads = 3
threads = []
for i in range(num_worker_threads):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)
source = [1,2,3,4,5]
for item in source:
    q.put(item)

# block until all tasks are done
q.join()

# stop workers
for i in range(num_worker_threads):
    q.put(None)
for t in threads:
    t.join()

#### concurent.futures
# https://docs.python.org/3.7/library/concurrent.futures.html
# ThreadPoolExecutor Example
import concurrent.futures
import urllib.request

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/']

# Retrieve a single page and report the URL and contents
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            print('%r page is %d bytes' % (url, len(data)))

#ProcessPoolExecutor Example

import concurrent.futures
import math

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]

def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))

if __name__ == '__main__':
    main()


#### asyncio
# https://docs.python.org/3/library/asyncio.html
# начиная с версии 3.7 получил много улучшений

import asyncio

async def hello1(name, timeout):
    await asyncio.sleep(timeout)
    print("Hello, {}".format(name))

async def hello2(name, timeout):
    await asyncio.sleep(timeout)
    print("Hello, {}".format(name))

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([hello1("Foo", 0.5), hello2("Baz", 0.1)]))

loop.run_until_complete(asyncio.gather(
    hello1("Bob", 0.5),
    hello2("Mike", 1.5)))
loop.close()


# потоки.
import asyncio

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)

    print(f'Send: {message!r}')
    writer.write(message.encode())

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()
    await writer.wait_closed()

asyncio.run(tcp_echo_client('Hello World!'))


#### Gevent
#http://www.gevent.org

import gevent

def foo():
    print('Running in foo')
    gevent.sleep(0)
    print('Explicit context switch to foo again')

def bar():
    print('Explicit context to bar')
    gevent.sleep(0)
    print('Implicit context switch back to bar')

gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar)])


# скачивание из сети
import gevent.monkey
gevent.monkey.patch_socket()
from gevent.pool import Pool
import requests


def fetch(url):
    response = requests.request('GET', url, timeout=5.0)
    print "Status: [%s] URL: %s" % (response.status_code, url)

    threads = []
    for i in range(1,10):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)


# Фреймворк для асинхронной работы Twisted
# https://pypi.org/project/Twisted/
# examples/twisted-server.py twisted-client.py


#### Celery
# распределенные вычисления
# https://pypi.org/project/celery/
# распределенные вычисления
from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y


# celery -A tasks worker --loglevel=info

from tasks import add
add.delay(4, 4)


## Ускорение работы интерпретатора
### pypy
# http://pypy.org/

### Cython
#https://cython.org/
# pip install cython
# пример examples/cython/fib.pyx

#Код на Python
def fib(n):
    """Print the Fibonacci series up to n."""
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b

    print()

# Использование С++
from libcpp.vector cimport vector

def primes(unsigned int nb_primes):
    cdef int n, i
    cdef vector[int] p
    p.reserve(nb_primes)  # allocate memory for 'nb_primes' elements.
    n = 2
    while p.size() < nb_primes:  # size() for vectors is similar to len()
        for i in p:
            if n % i == 0:
                break
        else:
            p.push_back(n)  # push_back is similar to append()
        n += 1
    # Vectors are automatically converted to Python
    # lists when converted to Python objects.
    return p

### numba
# http://numba.pydata.org/
# pip install numba

# Обычная версия
def naive_sum(x, y):
    ans = np.empty_like(x)
    for i in range(len(x)) :
        ans[i] = x[i] + y[i]
    return ans

# Версия с использованием numba
from numba import jit
@jit
def naive_sum_numba(x, y):
    ans = np.empty_like(x)
    for i in range(len(x)):
        ans[i] = x[i] + y[i]
    return ans

import time
import numpy as np
x = np.ones(1000000)
y = np.ones(1000000)
s=time.time()
naive_sum(x, y)
t1 = time.time() - s
s=time.time()
naive_sum_numba(x, y)
t2 = time.time()- s
speedup = t1/t2
print(speedup)

#Использовать специальные библиотеки. Например: numpy, scipy, pandas


"""
Материал для дополнительного изучения:

Работа с базой данных
https://habrahabr.ru/post/321510/

Учимся писать многопоточные и многопроцессные приложения на Python 
http://habrahabr.ru/post/149420/

Asyncio
https://itvdn.com/ru/blog/article/module-asyncio-python

AsyncIO для практикующего python-разработчика
https://habrahabr.ru/post/337420/

Gevent для практикующего питониста
https://vovkd.github.io/gevent-tutorial/

Фреймворк Twisted
https://habrahabr.ru/post/97201/

"""
