import cmath
if __name__ == '__main__':
    n = complex(input())
    r = cmath.polar(n)
    print(r[0])
    print(r[1])