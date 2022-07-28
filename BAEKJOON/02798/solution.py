# https://www.acmicpc.net/problem/2798

from itertools import combinations

n, m = [int(x) for x in input().split()]
a = [int(y) for y in input().split()]
ans = 0
for c in combinations(a, 3):
    s = sum(c)
    if s <= m and s > ans:
        ans = s

print(ans)
