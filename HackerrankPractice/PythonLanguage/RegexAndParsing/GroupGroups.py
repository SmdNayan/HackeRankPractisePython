import re
if __name__ == '__main__':
    s = re.search(r"([a-zA-Z0-9])\1", input())
    print(s.group(1) if s else -1)