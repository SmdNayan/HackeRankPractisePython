from collections import defaultdict
if __name__ == '__main__':
    n, m = map(int, input().split())
    d = defaultdict(list)
    for i in range(1, n+1):
        d[input()].append(str(i))
    # for i in range(m):
    #     print(' '.join(d[input()]) or -1)

    for _ in range(m): print(*d[input()] or [-1])

    # d = defaultdict(list)
    #
    # n, m = map(int, raw_input().split())
    #
    # for i in range(1, n + 1):
    #     d[raw_input()].append(str(i))
    #
    # for i in range(m):
    #     print(' '.join(d[raw_input()]) or -1)