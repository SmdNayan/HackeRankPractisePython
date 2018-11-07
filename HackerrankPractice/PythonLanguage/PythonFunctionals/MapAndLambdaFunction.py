
cube = lambda x: x**3# complete the lambda function
def fibonacci(n):
    # return a list of fibonacci numbers
    ls = [0, 1]
    for i in range(2, n):
        ls.append(ls[i-2] + ls[i-1])
    return ls[0:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))