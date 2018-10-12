from collections import Counter
from operator import itemgetter

if __name__ == '__main__':
    s = input()
    count_s = sorted(Counter(s).items())
    count_s.sort(key=itemgetter(1), reverse=True)
    for item in count_s[:3]:
        print(*item)