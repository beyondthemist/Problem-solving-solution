# https://www.acmicpc.net/problem/2477

k = int(input())
sides = []
for _ in range(6):
    sides.append([int(x) for x in input().split()])

prev = sides[-1]
area = ((max(sides, key=lambda s: s[1] if s[0] > 2 else -1)[1])
        * (max(sides, key=lambda s: s[1] if s[0] <= 2 else -1)[1]))
for i in range(0, 6):
    cur = sides[i]
    if ((prev[0] == 1 and cur[0] == 3)
        or (prev[0] == 2 and cur[0] == 4)
        or (prev[0] == 3 and cur[0] == 2)
        or (prev[0] == 4 and cur[0] == 1)):
        area -= (prev[1]*cur[1])
        break
    prev = cur

print(area*k)
