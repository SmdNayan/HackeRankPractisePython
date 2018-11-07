from collections import OrderedDict
if __name__ == '__main__':
    D = OrderedDict()
    for i in range(int(input())):
        w = input()
        D[w] = D.get(w, 0) + 1
    print(len(D))
    print(*D.values())