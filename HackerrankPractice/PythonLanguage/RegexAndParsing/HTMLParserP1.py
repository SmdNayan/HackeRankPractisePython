from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attr):
        print('Start :', tag)
        for e in attr:
            print('->', e[0], '>', e[1])
    def handle_endtag(self, tag):
        print('End   :', tag)
    def handle_startendtag(self, tag, attr):
        print('Empty :', tag)
        for e in attr:
            print('->', e[0], '>', e[1])

if __name__ == '__main__':
    parser = MyHTMLParser()
    for _ in range(int(input())):
        parser.feed(input())