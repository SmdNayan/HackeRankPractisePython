import numpy
if __name__ == '__main__':
    n = list(map(float, input().split()))
    numpy.set_printoptions(sign= ' ')
    print(numpy.floor(n))
    print(numpy.ceil(n))
    print(numpy.rint(n))