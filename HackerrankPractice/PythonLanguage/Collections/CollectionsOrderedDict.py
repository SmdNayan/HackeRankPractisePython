# Problem name is Collections.OrderedDict()
# An OrderedDict is a dictionary that remembers the order of the keys that were inserted first.
# If a new entry overwrites an existing entry, the original insertion position is left unchanged.

from collections import OrderedDict

if __name__ == '__main__':
    D = OrderedDict()
    for i in range(int(input())):
        *item, price = input().split()
        item = ' '.join(item)
        D[item] = D.get(item, 0) + int(price)

    for i, p in D.items():
        print(i, p)
