
def wrapper(f):
    def fun(l):
        for p in sorted([s[-10:] for s in l]):
            print("+91 " + p[0:5] + " " + p[5:])
        return
    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
