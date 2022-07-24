# https://www.acmicpc.net/problem/1912

n = int(input())
a = [int(x) for x in input().split()]
m = [a[0]]

for i in range(1, n):
    m.append(max(m[-1] + a[i], a[i]))

print(max(m))
