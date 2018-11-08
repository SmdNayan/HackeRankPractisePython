# Complete the plusMinus function below.
def plusMinus(arr):
    zero =0
    positiv = 0
    negative = 0
    for i in range(n):
        if arr[i] == 0:
            zero +=1
        elif arr[i] < 0:
            negative +=1
        else:
            positiv +=1

    print("{0:.6f}".format(round(positiv/len(arr), 6)))
    print("{0:.6f}".format(round(negative / len(arr), 6)))
    print("{0:.6f}".format(round(zero / len(arr), 6)))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)