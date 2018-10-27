import numpy

if __name__ == '__main__':
    arr = numpy.array(list(map(int, input().split())))
    arr.shape = (3, 3)
    print(arr)