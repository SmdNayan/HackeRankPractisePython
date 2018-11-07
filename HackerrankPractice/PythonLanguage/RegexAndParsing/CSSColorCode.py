import re
if __name__ == '__main__':
    for _ in range(int(input())):
        s = re.findall(r'#[0-9a-fA-F]{3,6}', input()[1:])
        if len(s):
            print(*s, sep='\n')