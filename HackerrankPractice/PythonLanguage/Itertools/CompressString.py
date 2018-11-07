from itertools import groupby
if __name__ == '__main__':
    s = input()
    for n, l in groupby(s):
        print('({}, {})'.format(len(list(l)),n),end=' ')