#### concurent.futures
import urllib.request
import shutil
import argparse
import os
from html.parser import HTMLParser

number_of_starttags = 0
number_of_endtags = 0
rezults_tag = []

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global number_of_starttags
        print('<',tag, '>')
        rezults_tag.append(tag)
        number_of_starttags += 1

    def handle_endtag(self, tag):
        global number_of_endtags
        print('</',tag, '>')
        rezults_tag.append(tag)
        number_of_endtags += 1

def main():
    # # procassing input parameters
    parser = argparse.ArgumentParser(description='Programm to work with AWS')
    parser.add_argument('--get', help='gathering info about this site')
    parser.add_argument('--view', help='displaying info about this site')
    args = parser.parse_args()

    if args.get == '' :
        print('see next time. bye')
        exit(0)


    url = 'https://12factor.net/ru/config'
    output_file = "12factor.html"
    response = urllib.request.urlopen(url)
    webContent = response.read()
    print(webContent[0:3000])

    f = open( output_file, 'wb')
    f.write(webContent)
    f.close
    print(os.getcwd())

    # instantiate the parser and fed it some HTML
    parser = MyHTMLParser()
    # parser.feed(webContent)
    with open(output_file, encoding="utf-8") as f:
        for line in f:
            parser.feed(line)

    print('')
    print(rezults_tag)
    print('Tegs total: ', len(rezults_tag))
    rezults_tag_list = list(dict.fromkeys(rezults_tag))
    print('uniq tags list: ', rezults_tag_list)
    rezults_tag_dict = {r_tag:rezults_tag.count(r_tag) for r_tag in rezults_tag_list}
    print('Tags frequency: ', rezults_tag_dict)
    print('Tegs total final: ', sum(rezults_tag_dict.values()))


    print(list(dict.fromkeys(rezults_tag)))
    print(number_of_starttags, number_of_endtags)

# r0 = ['html', 'head', 'meta', 'title', 'title', 'meta', 'meta', 'meta', 'link', 'link', 'link', 'script', 'script', 'script', 'script', 'head', 'body', 'noscript', 'iframe', 'iframe', 'noscript', 'script', 'script', 'header', 'h1', 'a', 'a', 'h1', 'header', 'section', 'article', 'h2', 'h2', 'h3', 'h3', 'p', 'em', 'em', 'a', 'a', 'p', 'ul', 'li', 'a', 'a', 'li', 'li', 'li', 'li', 'li', 'ul', 'p', 'strong', 'strong', 'p', 'p', 'p', 'p', 'strong', 'strong', 'a', 'a', 'a', 'a', 'p', 'p', 'p', 'p', 'strong', 'em', 'em', 'strong', 'em', 'em', 'em', 'em', 'p', 'p', 'code', 'code', 'code', 'code', 'code', 'code', 'code', 'code', 'code', 'code', 'code', 'code', 'p', 'p', 'p', 'article', 'section', 'section', 'nav', 'div', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'span', 'span', 'div', 'div', 'a', 'a', 'div', 'div', 'a', 'a', 'div', 'nav', 'section', 'footer', 'div', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'span', 'span', 'div', 'div', 'div', 'div', 'div', 'div', 'a', 'a', 'div', 'div', 'a', 'a', 'div', 'div', 'a', 'a', 'div', 'footer', 'body', 'html']
# len(r0)
# r1 = list(dict.fromkeys(r0))
# r2 = {r_tag:rezult.count(r_tag) for r_tag in r1}
# print(r2)
# sum(r2.values())


if __name__ == "__main__":
    # execute only if run as a script
    main()
