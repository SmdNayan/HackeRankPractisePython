import numpy
if __name__ == '__main__':
    n, m = map(int, input().split())
    n_array = numpy.array([input().split() for i in range(n)],int)
    numpy.set_printoptions(legacy='1.13')
    print(numpy.mean(n_array,axis=1),numpy.var(n_array,axis=0),numpy.std(n_array),sep="\n")