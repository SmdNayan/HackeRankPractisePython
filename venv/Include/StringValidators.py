if __name__ == '__main__':
    s = input()
    count = [0, 0, 0, 0, 0]
    for i in s:
        count[0] += 1 if i.isalnum() else False
        count[1] += 1 if i.isalpha() else False
        count[2] += 1 if i.isdigit() else False
        count[3] += 1 if i.islower() else False
        count[4] += 1 if i.isupper() else False

    print(True if count[0] > 0 else False)
    print(True if count[1] > 0 else False)
    print(True if count[2] > 0 else False)
    print(True if count[3] > 0 else False)
    print(True if count[4] > 0 else False)
