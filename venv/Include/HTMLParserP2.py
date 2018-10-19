from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if len(data.split('\n')) == 1:
            print('>>> Single Line Comment', data, sep='\n')
        else:
            print('>>> Multi-line Comment', data, sep='\n')
    def handle_data(self, data):
        if data != '\n':
            print('>>> Data', data, sep='\n')
if __name__ == '__main__':
    html = ""
    for i in range(int(input())):
        html += input().rstrip()
        html += '\n'

    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()