if __name__ == '__main__':
    n = int(input())
    ns = set(map(int, input().split(' ')))
    nc = int(input())
    for i in range(nc):
        st, *arg = map(str, input().split())
        if(st == 'pop'):
            ns.pop()
        elif (st == 'remove'):
            ns.remove(int(arg[0]))
        else:
            ns.discard(int(arg[0]))
    print(sum(ns))
