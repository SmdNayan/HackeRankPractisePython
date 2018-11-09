import datetime

def timeConversion(s):
    dt = datetime.datetime.strptime(s, '%I:%M:%S%p')
    return dt.strftime('%H:%M:%S')

if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
    print(result)