n = int(input())
a = []
for i in range(n):
    a.append([int(x) for x in input().split()])

for i in range(n - 2, -1, -1):
    for j in range(i + 1):
        a[i][j] += max(a[i + 1][j], a[i + 1][j + 1])

print(a[0][0])
