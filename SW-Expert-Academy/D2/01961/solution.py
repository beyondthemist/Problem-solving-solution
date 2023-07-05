def rotate(a, n):
    temp = [['X' for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            temp[j][n - i - 1] = a[i][j];
        
    return [''.join(temp[i]) for i in range(n)]


t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    a = [input().split() for _ in range(n)]
    ans = [['X' for i in range(3)] for j in range(n)]

    for j in range(3):
        a = rotate(a=a, n=n)

        for i in range(n):
            ans[i][j] = a[i]

    print(f'#{test_case}')
    for b in ans:
        print(' '.join(b))
