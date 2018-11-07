if __name__ == '__main__':

    n1 = int(input())
    a = set(input().split(' '))
    n2 = int(input())
    b = set(input().split(' '))

    d1 = a.difference(b)
    d2 = b.difference(a)
    u = d1.union(d2)
    print('\n'.join(sorted(u, key=int)))

