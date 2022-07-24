# https://www.acmicpc.net/problem/9461

m = 0
i = []
for _ in range(int(input())):
    i.append(int(input()))
    if m < i[-1]:
        m = i[-1]

a = [1, 1, 1] # sentinel

for _ in range(4, m + 1):
    a.append(a[-2] + a[-3])

for x in i:
    print(a[x - 1])
