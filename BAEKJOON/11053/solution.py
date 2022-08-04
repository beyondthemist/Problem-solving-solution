n = int(input())
a = [int(x) for x in input().split()]
d = [1 for _ in range(n)]

for curr in range(n):
    for prev in range(curr):
        if a[prev] < a[curr] :
            d[curr] = max(d[curr], 1 + d[prev])

print(max(d))
