import numpy
if __name__ == '__main__':

    n, m = map(int, input().split())
    arr = numpy.array([input().split() for i in range(n)], int)
    s_arr = numpy.sum(arr, axis=0)
    print(numpy.prod(s_arr, axis=0))