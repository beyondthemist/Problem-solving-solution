# https://www.acmicpc.net/problem/7568

n = int(input())
a = [[int(x) for x in input().split()] for _ in range(n)]
'''a = []
for _ in range(n):
    a.append([int(x) for x in input().split()])'''

for i in range(n):
    count = 0
    for j in range(n):
        count += int(a[i][0] < a[j][0]
                     and a[i][1] < a[j][1])
    a[i].append(count + 1)

print(' '.join([str(x[2]) for x in a]))
