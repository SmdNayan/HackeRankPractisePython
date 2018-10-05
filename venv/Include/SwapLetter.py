def swap_case(s):
    l = len(s)
    j=""
    for i in range(l):
        if (s[i] == s[i].upper()):
            j += s[i].lower()
        elif (s[i] == s[i].lower()):
            # print(s[i].upper())
            # j.replace(s[i], s[i].upper())
            j += s[i].upper()

    return j

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)