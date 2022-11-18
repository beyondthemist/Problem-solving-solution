import sys 
input = sys.stdin.readline

n = int(input())
m, k = [int(x) for x in input().split()]
a = sorted([int(x) for x in input().split()], reverse=True)

if sum(a) < m*k:
    print('STRESS')
else:
    s = 0
    for i in range(n):
        s += a[i]
        if s >= m*k:
            print(i + 1)
            break
