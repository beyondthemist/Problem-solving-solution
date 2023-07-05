t = int(input())
for test_case in range(1, t + 1):
    answers = []
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(y) for y in input().split()]

    if n == m:
        ans = 0
        for x, y in zip(a, b):
            ans += x*y
            print(f'#{test_case} {ans}')
            continue
    elif n > m:
        a, b = b, a
        n, m = m, n

    ans = -1
    for i in range(n - 1, m):
        temp = 0
        for j in range(n):
            temp += a[j] * b[i - n + 1 + j]
        if ans < temp:
            ans = temp
    print(f'#{test_case} {ans}')
