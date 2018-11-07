if __name__ == '__main__':
    n = int(input())
    s1 = set(map(int, input().split()))
    o = int(input())
    for i in range(o):
        st, arg = input().split()
        s2 = set(map(int, input().split()))
        if(st == 'intersection_update'):
            s1.intersection_update(s2)
        elif (st == 'update'):
            s1.update(s2)
        elif (st == 'symmetric_difference_update'):
            s1.symmetric_difference_update(s2)
        elif(st == 'difference_update'):
            s1.difference_update(s2)


    print(sum(s1))