if __name__ == '__main__':
    s = set(map(int, input().split()))
    n = int(input())
    res= []
    result = True
    for i in range(n):
        ns = set(map(int, input().split()))
        if (s.issuperset(ns)):
            res.append(True)
        else:
            res.append(False)

    for i in range(len(res)):
        if (res[i] == False):
            result = False
    print(result)
