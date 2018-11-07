import re

if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix, s = [], ''
    for i in range(n):
        matrix.append(input())
    for a in zip(*matrix):
        s += ''.join(a)
    print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", s))
