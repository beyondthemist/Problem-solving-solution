# https://www.acmicpc.net/problem/1002

from math import dist

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = [int(i) for i in input().split()]
    d = dist([x1, y1], [x2, y2])

    if d == 0:
        print('-1' if r1 == r2 else '0')
    elif abs(r1 - r2) < d and d < r1 + r2:
        print('2')
    elif d == r1 + r2 or d == abs(r1 - r2):
        print('1')
    elif r1 + r2 < d or d < abs(r1 - r2):
        print('0')
