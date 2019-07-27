## Сетевое программирование

### Низкоуровневая работа с сокетами

#### sockets
# https://docs.python.org/3/library/socket.html

## server
import socket
sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()
print('connected:', addr)
while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data.upper())
conn.close()

# client
import socket
sock = socket.socket()
sock.connect(('localhost', 9090))
sock.send('hello, world!')
data = sock.recv(1024)
sock.close()
print(data)

### Протокол http
# https://docs.python.org/3/library/http.html

# http.server
# python -m http.server 8000

import http.server
import socketserver

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()

# http.client

import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
resp = conn.getresponse()
resp.code
resp.length


### SMTP
# https://docs.python.org/3/library/smtplib.html
import smtplib
msg = "From: e@mail\r\nTo: e@mail\r\n\r\nText"
server = smtplib.SMTP('localhost')
server.sendmail("from@addr", "to@addr", msg)
server.quit()

### Модуль email

### POP3
# https://docs.python.org/3/library/poplib.html
# https://docs.python.org/3/library/getpass.html
import getpass, poplib
M = poplib.POP3('localhost')
M.user(getpass.getuser())
M.pass_(getpass.getpass())
numMessages = len(M.list()[1])
for i in range(numMessages):
    for j in M.retr(i+1)[1]:
        print j


### IMAP
# https://docs.python.org/3/library/imaplib.html
import getpass, imaplib
M = imaplib.IMAP4()
M.login(getpass.getuser(), getpass.getpass())
M.select()
typ, data = M.search(None, 'ALL')
for num in data[0].split():
    typ, data = M.fetch(num, '(RFC822)')
    print 'Message %s\n%s\n' % (num, data[0][1])
M.close()
M.logout()


### urllib.request
# https://docs.python.org/3/library/urllib.html

### requests
# https://pypi.org/project/requests/
import requests
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
r.status_code
r.text
r = requests.get('http://ya.ru')
r.status_code
r.text


### WSGI web фреймворки

# WEB серверы
# протокол WSGI
# https://pypi.org/project/gunicorn/
# gunicorn
# nginx -> gunicorn -> scrypt.py

#### Bottle
# https://pypi.org/project/bottle/
#examples/mybottle.py

#### Flask
# https://pypi.org/project/flask/
#examples/myflask.py

#### Django
# https://pypi.org/project/django/
#examples/django.py


### Async web фреймворки
#### tornado
# https://pypi.org/project/tornado/
#Tornado is a Python web framework and asynchronous networking library,
# Here is a simple “Hello, world” example web app for Tornado:

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


#### aiohttp
# https://pypi.org/project/aiohttp/
# https://aiohttp.readthedocs.io
# Client and HTTP Server.
# Server WebSockets and Client WebSockets
#pip install aiohttp

#Client example:

import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://python.org')
        print(html)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

# Server example:

from aiohttp import web

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle)])

web.run_app(app)


## Кроссплатформенная разработка

### Встроенные модули
#### os
# https://docs.python.org/3/library/os.html
# операции специфические для ОС
# атрибуты файлов
import os
os.path
os.name
# os.path - работа с путями к файлам
os.path.join("pathfile","output","log.txt")
os.path.isfile('/root')
os.path.exists('/path')

#### tempfile
# https://docs.python.org/3/library/tempfile.html
# create a temporary file using a context manager
import tempfile
with tempfile.TemporaryFile() as fp:
    fp.write(b'Hello world!')
    fp.seek(0)
    data = fp.read()
    print(data)

#### shutil
# https://docs.python.org/3/library/shutil.html
# Коприрование, файлов, каталогов, работа с архивами
import os, stat
import shutil
def remove_readonly(func, path, _):
    "Clear the readonly bit and reattempt the removal"
    os.chmod(path, stat.S_IWRITE)
    func(path)

shutil.rmtree(directory, onerror=remove_readonly)

from shutil import make_archive
import os
archive_name = os.path.expanduser(os.path.join('~', 'myarchive'))
root_dir = os.path.expanduser(os.path.join('~', '.ssh'))
make_archive(archive_name, 'gztar', root_dir)
'/Users/kostya/myarchive.tar.gz'


#### platform
# https://docs.python.org/3/library/platform.html
import platform
platform.python_version()
platform.machine()
platform.platform()

### kivy
# https://kivy.org/

# установка
# примеры
# tutorials
# demo
# API


"""
Материал для дополнительного изучения:

Сокеты в Python для начинающих  
http://habrahabr.ru/post/149077/

Bottle
https://habrahabr.ru/post/221659/

Flask
https://ru.code-maven.com/hello-world-with-flask-and-python
http://flask-russian-docs.readthedocs.io/ru/latest/quickstart.html

Django
https://tutorial.djangogirls.org/ru/django_start_project/
http://djbook.ru/rel1.4/intro/tutorial01.html

Tornado vs Aiohttp: путешествие в дебри асинхронных фреймворков
https://habr.com/ru/company/avito/blog/435532/

Kivy
https://habrahabr.ru/post/314236/

Python quiz
http://quizbucket.org/quiz/python/list-questions

Improve Your Python Skills
https://dbader.org/

Каталог библиотек питона для разных задач
https://awesome-python.com/

Пишем платформер на Python, используя pygame 
http://habrahabr.ru/post/193888/

Как написать дополнение для GIMP на языке Python 
http://habrahabr.ru/post/135863/
"""