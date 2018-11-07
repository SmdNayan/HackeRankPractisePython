import numpy

if __name__ == '__main__':
    n, m = map(int, input().split())
    array = numpy.array([input().split() for i in range(n)], int)
    print(array.transpose())
    print(array.flatten())