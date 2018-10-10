from itertools import combinations
if __name__ == '__main__':
    n = int(input())
    sl = list(input().split())
    k = int(input())

    f= []
    l1 = list(combinations(sl,k))
    for i in l1:
        if ('a' in i):
            f.append(i)
    print(len(f)/len(l1))
