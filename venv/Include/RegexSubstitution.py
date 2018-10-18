import re
if __name__ == "__main__":
    for i in range(int(input())):
        s = input()
        ss = re.sub(r'(?<=\s)&&(?=\s)', 'and', s)
        sss = re.sub(r'(?<=\s)[|]{2}(?=\s)', 'or', ss)
        print(sss)