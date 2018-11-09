
if __name__ == '__main__':
    lst = list(map(int, input().split(' ')))
    num = sum(lst)
    print((num-(max(lst))), (num-(min(lst))))