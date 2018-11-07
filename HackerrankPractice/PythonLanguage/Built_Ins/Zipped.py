if __name__ == '__main__':
    a, y = map(int, input().split())
    score = []
    for i in range(y):
        score.append(list(map(float, input().split())))
    for i in zip(*score):
        print(sum(i)/len(i))