from datetime import datetime

if __name__ == '__main__':
    for i in range(int(input())):
        t1 = datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
        t2 = datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
        print(int(abs((t1 - t2).total_seconds())))