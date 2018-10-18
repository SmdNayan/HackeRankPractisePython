import re
if __name__ == '__main__':
    s, w = input(), input()
    p = re.compile(w)
    r = p.search(s)
    if not r:
        print("(-1, -1)")
    while r:
        print("({0}, {1})".format(r.start(), r.end() -1))
        r = p.search(s, r.start() + 1)
