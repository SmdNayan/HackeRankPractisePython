import  re
if __name__ == '__main__':
    for i in range(int(input())):
        s = input()
        r = True
        try:
            re.compile(s)
        except Exception:
            r = False
        print(r)