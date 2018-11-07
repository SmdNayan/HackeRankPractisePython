from collections import Counter
if __name__ == '__main__':
    x = int(input())
    sh = Counter(map(int, input().split()))
    n = int(input())
    inc = 0
    for i in range(n):
        shS, ShV =  map(int, input().split())
        if sh[shS]:
            inc += ShV
            sh[shS] -=1
    print(inc)