#Problem name is Collections.namedtuple()

from collections import namedtuple
if __name__ == '__main__':
    n, categories= int(input()), input().split()
    total =0
    for i in range(n):
        students = namedtuple('Student', categories)
        c1, c2, c3, c4 = input().split()
        Student = students(c1, c2, c3, c4)
        total += int(Student.MARKS)
    print(total/n);