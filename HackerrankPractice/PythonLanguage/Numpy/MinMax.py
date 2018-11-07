import numpy
if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = numpy.array([input().split() for i in range(n)], int)
    min_arr = numpy.min(arr, axis=1)
    print(numpy.max(min_arr, axis=0))