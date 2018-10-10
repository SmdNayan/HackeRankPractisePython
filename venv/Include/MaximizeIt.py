from itertools import product
if __name__ == '__main__':
    n, m = map(int, input().split())
    k = []
    for i in range(n):
        k.append(list(map(int, input().split())))

    c= list(product(*k))
    r = [sum([y ** 2 for y in x]) % m for x in c]
    print(r)
    print(max(r))
    # for i in range(len(k)):
    #     j.append(max(k[i]))
    # r = []
    # sum=0
    # for i in range(len(j)):
    #     a = j[i]**2
    #     sum += a
    #     r.append(sum%m)
    # print(max(r))



    # K, M = list(map(int, input().split()))
    # l = []
    # for i in range(K):
    #     l.append(list(map(int, input().split()))[1:])
    #     # Compute the cross product
    # cross = list(itertools.product(*l))
    # # get the different remainder for different combinations of items when divided by M
    # remainder = [sum([y ** 2 for y in x]) % M for x in cross]
    # # Print the maximum remainder
    # print(max(remainder))