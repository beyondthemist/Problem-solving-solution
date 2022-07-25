# https://www.acmicpc.net/problem/2579

n = int(input())

if n == 1:
    print(int(input()))
else:
    a = [0]*(n + 1)
    d = [0]*(n + 1)
    for i in range(1, n + 1):
        a[i] = int(input())

    d[1] = a[1]
    d[2] = max(a[2] + a[1], a[2])
    for i in range(3, n + 1):
        d[i] = max(a[i] + a[i - 1] + d[i - 3], a[i] + d[i - 2])
        
    print(d[-1])
