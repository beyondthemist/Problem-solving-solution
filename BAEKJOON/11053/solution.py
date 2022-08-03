n = int(input())
a = [int(x) for x in input().split()]
d = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            d[i] = max(d[i], 1 + d[j])

print(max(d))
