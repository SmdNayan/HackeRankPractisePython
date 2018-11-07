import numpy
if __name__ == '__main__':
    a = list(map(float, input().split()))
    x = float(input())
    print(numpy.polyval(a, x))
