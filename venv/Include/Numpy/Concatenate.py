import numpy
if __name__ == '__main__':
    n, m, p = map(int, input().split())
    arr1 = numpy.array([input().split() for i in range(n)],int)
    arr2 = numpy.array([input().split() for i in range(m)],int)
    print(arr1)
    print(numpy.concatenate((arr1, arr2), axis = 0))