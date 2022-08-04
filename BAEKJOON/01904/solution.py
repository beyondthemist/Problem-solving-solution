# https://www.acmicpc.net/problem/1904

x, y = 1, 1
for _ in range(int(input()) - 1):
    x, y = y, x
    y = (x + y)%15746

print(y)
