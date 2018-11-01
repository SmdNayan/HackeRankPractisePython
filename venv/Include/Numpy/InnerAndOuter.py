import numpy
if __name__ == '__main__':
    A, B = [numpy.array([input().split()], int) for i in range(2)]
    print(numpy.inner(A, B)[0][0], numpy.outer(A, B), sep="\n")