if __name__ == '__main__':
    t = int(input())
    for i in range(t+1):
        n = int(input())
        ns = set(map(int, input().split()))
        n2 = int(input())
        n2s = set(map(int, input().split()))

        print(ns.issubset(n2s))
