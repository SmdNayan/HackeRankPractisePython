import math
if __name__ == '__main__':
    AB = int(input())
    BC = int(input())

    res = math.degrees(math.atan2(AB, BC))

    print(str(int(round(res))) + "°")

