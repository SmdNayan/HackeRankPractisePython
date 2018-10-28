import numpy

if __name__ == '__main__':
    num = tuple(map(int, input().split()))
    print(numpy.zeros(num, dtype= int))
    print(numpy.ones(num, dtype=int))