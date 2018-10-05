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

    count = 0

    n, m = input().split()
    hc = [int(x) for x in input().split()]
    A = set([int(y) for y in input().split()])
    B = set([int(z) for z in input().split()])
    count = [count + 1 if x in A else count - 1 if x in B else count + count for x in hc]
    print(sum(count))

    n, m = [int(x) for x in input().split()]
    arr = ([int(x) for x in input().split()])
    a = set([int(x) for x in input().split()])
    b = set([int(x) for x in input().split()])
    happiness = 0

    for i in arr:
        if i in a:
            happiness += 1
        if i in b:
            happiness -= 1

    print(happiness)

    n, m = map(int, (input().strip().split(' ')))
    arr = list(map(int, (input().strip().split(' '))))
    A = set(list(map(int, (input().strip().split(' ')))))
    B = set(list(map(int, (input().strip().split(' ')))))

    H = 0

    for i in arr:
        if i in A:
            H += 1
        if i in B:
            H -= 1

    print(H)