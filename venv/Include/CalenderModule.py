import datetime
if __name__ == '__main__':
    n = input()
    d = datetime.datetime.strptime(n, '%m %d %Y').strftime('%A')
    print(d.upper())