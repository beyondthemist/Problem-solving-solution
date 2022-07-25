# https://www.acmicpc.net/problem/2217

n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

a.sort()
m = 0
for i in range(len(a)):
    if m < (n - i)*a[i]:
        m = (n - i)*a[i]
print(m)
