# https://www.acmicpc.net/problem/1912

n = int(input())
a = [int(x) for x in input().split()]
m = a[0]
ans = a[0]

for i in range(1, n):
    m = max(m + a[i], a[i])
    if ans < m:
        ans = m

print(ans)
