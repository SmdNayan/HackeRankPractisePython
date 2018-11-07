from collections import deque
if __name__ == '__main__':
    for i in range(int(input())):
        l = int(input())
        d = deque(map(int, input().split()))
        for _ in range(int(l-1)):
            if d[0] >= d[1]:
                d.popleft()
            elif d[-1] >= d[-2]:
                d.pop()
        if len(d) > 1:
            print('No')
        else:
            print('Yes')
