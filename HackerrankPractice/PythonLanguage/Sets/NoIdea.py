if __name__ == '__main__':

    n, m = map(input().split())
    hc = input().split(' ')
    a = set(input().split(' '))
    b = set(input().split(' '))

    h = 0

    for i in hc:
        if (i in a):
            h = h + 1
        if (i in b):
            h = h - 1
    print(h)
