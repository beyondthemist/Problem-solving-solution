# https://www.acmicpc.net/problem/1003

for i in range(int(input())):
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    count = 0
    for j in range(int(input())):
        cx, cy, r = [int(z) for z in input().split()]
        if ((x1 - cx)**2 + (y1 - cy)**2 <= r**2) ^ ((x2 - cx)**2 + (y2 - cy)**2 <= r**2):
            count += 1
    print(count)
