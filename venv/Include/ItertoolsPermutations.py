from itertools import permutations
if __name__ == '__main__':
    s, n = input().split()
    print(*[''.join(i) for i in permutations(sorted(s), int(n))], sep='\n')