# https://www.acmicpc.net/problem/2748

n = int(input())
x, y = 0, 1
for i in range(2, n + 1):
    x, y = y, x
    y = x + y
print(y)
