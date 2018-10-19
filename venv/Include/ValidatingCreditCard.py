import re

if __name__ == '__main__':
    p = re.compile(r'^(?!.*(\d)(-?\1){3})([456])(\d{3})((?:-?\d{4}){3})$')

    s = int(input())

    for _ in range(s):
        uid = input()
        print('Valid' if p.match(uid) else 'Invalid')