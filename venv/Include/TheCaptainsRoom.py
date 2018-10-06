if __name__ == '__main__':
    gn = int(input())
    rn = input().split()
    setUnique = set()
    uniqueRoomSet = set();

    for i in rn:
        if (i in setUnique):
            uniqueRoomSet.add(i)
        else:
            setUnique.add(i)
    print(setUnique.difference(uniqueRoomSet).pop())

