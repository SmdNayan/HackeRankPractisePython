from collections import defaultdict
if __name__ == '__main__':
    n, m = map(int, input().split())
    d = defaultdict(list)
    for i in range(1, n+1):
        d[input()].append(str(i))

    for _ in range(m): print(*d[input()] or [-1])
