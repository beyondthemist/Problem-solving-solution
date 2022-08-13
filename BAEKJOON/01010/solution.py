t = int(input())
for _ in range(t):
    n, m = [int(x) for x in input().split()]

    res = 1
    for i in range(1, (min(m - n, n) + 1)): # mCn
        res *= (m - (i - 1))
        res //= i

    print(res)
