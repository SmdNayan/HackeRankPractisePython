import re
if __name__ == '__main__':
    for i in range(int(input())):
        print('YES' if re.match(r'[789]\d{9}$', input()) else 'NO')

#         if re.match(r'[789]\d{9}$',raw_input()):
#     print 'YES'
# else:
#     print 'NO'