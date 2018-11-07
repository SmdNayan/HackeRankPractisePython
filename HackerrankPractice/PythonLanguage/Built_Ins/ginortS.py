
if __name__ == '__main__':
    sList = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468"
    print(*sorted(input(), key=sList.index), sep='')