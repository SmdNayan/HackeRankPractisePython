def split_and_join(line):
    # write your code here
    s = line.split(" ")
    r = "-".join(s)
    return r

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)