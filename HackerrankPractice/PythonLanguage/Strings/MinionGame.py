def minion_game(string):
    vowels = 'AEIOU'

    kvn = 0
    strt = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kvn += (len(string)-i)
        else:
            strt += (len(string)-i)

    if kvn > strt:
        print("Kevin", kvn)
    elif kvn < strt:
        print("Stuart", strt)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)