# https://www.acmicpc.net/problem/4153

a, b, c = sorted([int(x) for x in input().split()])
while a != 0 and b != 0 and c != 0:
    print('right' if a**2 + b**2 == c**2 else 'wrong')
    a, b, c = sorted([int(x) for x in input().split()])
