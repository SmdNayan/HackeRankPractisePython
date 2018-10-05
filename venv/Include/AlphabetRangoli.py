import string
def print_rangoli(size):
    alpha = string.ascii_lowercase
    Lst = []
    for i in range(size):
        s = "-".join(alpha[i:n])
        Lst.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    print('\n'.join(Lst[:0:-1]+Lst))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)