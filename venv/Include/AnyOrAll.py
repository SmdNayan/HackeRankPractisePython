# any() This expression returns True if any element of the iterable is true. If the iterable is empty, it will return False.
# all() This expression returns True if all of the elements of the iterable are true. If the iterable is empty, it will return True.

if __name__ == '__main__':
    N, NL = int(input()), input().split()
    print(all([int(i) > 0 for i in NL]) and any([j == j[::-1] for j in NL]))