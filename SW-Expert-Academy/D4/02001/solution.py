#import sys
#input = sys.__stdin__.readline
#can't import sys

t = int(input())
for case in range(1, t + 1):
    n, m = [int(x) for x in input().split()]
    areas = []
    for __ in range(n):
        areas.append([int(x) for x in input().split()])
    
    ans = 0
    for i in range(0, n - m + 1):
        for j in range(0, n - m + 1):
            tmp = 0

            for p in range(i, i + m):
                for q in range(j, j + m):
                    tmp += areas[p][q]

            if ans < tmp:
                ans = tmp

    print(f'#{case} {ans}')
