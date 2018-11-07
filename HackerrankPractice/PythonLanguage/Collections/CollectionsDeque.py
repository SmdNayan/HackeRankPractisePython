from collections import deque
if __name__ == '__main__':
    d = deque()
    for i in range(int(input())):
         s, *v = input().split()
         getattr(d, s)(*v) #here getattr (d, s) means d.givenOpeation
    print(*d)