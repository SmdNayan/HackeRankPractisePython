if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list = list(arr)
    print(list)
    l = [x for x in list if x != max(list)]
    print(max(l))