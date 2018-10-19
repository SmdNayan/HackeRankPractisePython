import re

if __name__ == '__main__':
    p = re.compile(r'(?!.*(.).*\1)(?=.*\d.*\d.*\d)(?=.*[A-Z].*[A-Z])[A-Za-z0-9]{10}')
    s = int(input())

    for _ in range(s):
        uid = input()
        print('Valid' if p.match(uid) else 'Invalid')