import sys
input = sys.__stdin__.readline

n = int(input())
dp = [False, True, False, True]

if n <= 4:
    print('SK' if dp[n - 1] else 'CY')
else:
    for i in range(4, n):
        dp.append((not dp[-1]) or (not dp[-3]) or (not dp[-4]))
    print('SK' if dp[-1] else 'CY')
