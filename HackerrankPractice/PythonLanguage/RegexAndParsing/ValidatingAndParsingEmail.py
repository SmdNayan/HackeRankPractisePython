import re
import email.utils
if __name__ == '__main__':
    for _ in range(int(input())):
        k, s = input().split(' ')
        m = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>$', s)
        if m:
            print(k,s)