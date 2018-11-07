from itertools import combinations_with_replacement
if __name__ == '__main__':
    if __name__ == '__main__':
        s, n = input().split()
        s = sorted(s)
        for c in combinations_with_replacement(s, 2):
            print(''.join(c))