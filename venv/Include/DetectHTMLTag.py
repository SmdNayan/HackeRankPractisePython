from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for a in attrs:
            print('->', a[0], '>', a[1])

if __name__ == '__main__':
    parser = MyHTMLParser()
    for _ in range(int(input())):
        parser.feed(input())