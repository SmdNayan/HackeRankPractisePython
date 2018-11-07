

def average(array):
    # your code goes here
    st = set(array)
    s = sum(st)
    avg = s/len(st)
    print(st)
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)