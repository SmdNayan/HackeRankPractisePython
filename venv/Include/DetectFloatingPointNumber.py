import re
if __name__ == '__main__':
    patt = re.compile('^[-+]?[0-9]*\.[0-9]+$')
    for _ in range(int(input())):
        print(bool(patt.match(input())))