#https://www.acmicpc.net/problem/11399

t = int(input())
p = sorted([int(x) for x in input().split()], reverse=True)
s = 0
for i in range(t):
    s += ((i + 1)*p[i])
print(s)
