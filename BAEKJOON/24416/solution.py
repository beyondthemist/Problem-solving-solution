# https://www.acmicpc.net/problem/24416

n = int(input())
x, y = 1, 2
for i in range(3, n):
    x, y = y, x
    y = x + y
print(y, n - 2)
