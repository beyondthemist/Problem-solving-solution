T = 10
for test_case in range(1, T + 1):
    n = int(input())
    heights = [int(x) for x in input().split()]

    cnt = 0
    for i in range(2, n - 2):
        m = max(heights[i - 2], heights[i - 1], heights[i + 1], heights[i + 2])
        if heights[i] > m:
            cnt += heights[i] - m

    print(f'#{test_case} {cnt}')
