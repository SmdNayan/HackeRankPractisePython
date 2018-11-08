# Complete the compareTriplets function below.
def compareTriples(a, b):
    score = [0, 0]
    for a, b in zip(a, b):
        if a > b:
            score[0] += 1
        elif b > a:
            score[1] += 1
    return score


if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriples(a, b)
    print(result[0], result[1])
