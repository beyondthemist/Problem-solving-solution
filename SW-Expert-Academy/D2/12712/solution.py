t = int(input())

for test_case in range(1, t + 1):
    n, m = list(map(int, input().split()))
    flies = [[int(x) for x in input().split()] for _ in range(n)]
    answer = -1
    for i in range(n):
        for j in range(n):
            ans1 = flies[i][j]

            for offset in range(1, m):
                if j - offset >= 0:
                    ans1 += flies[i][j - offset]

                if j + offset < n:
                    ans1 += flies[i][j + offset]

                if i + offset < n:
                    ans1 += flies[i + offset][j]

                if i - offset >= 0:
                    ans1 += flies[i - offset][j]


            ans2 = flies[i][j]
            for offset in range(1, m):
                if i - offset >= 0 and j - offset >= 0:
                    ans2 += flies[i - offset][j - offset]

                if i - offset >= 0 and j + offset < n:
                    ans2 += flies[i - offset][j + offset]

                if i + offset < n and j + offset < n: 
                    ans2 += flies[i + offset][j + offset]

                if i + offset < n and j - offset >= 0:
                    ans2 += flies[i + offset][j - offset]

            if answer < ans1:
                answer = ans1
            
            if answer < ans2:
                answer = ans2

    print(f'#{test_case} {answer}')
