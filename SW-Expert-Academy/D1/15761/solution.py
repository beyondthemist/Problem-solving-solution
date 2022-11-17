t = int(input())
for case in range(1, t + 1):
    a, b = [int(x) for x in input().split()]

    M = int(''.join((['1']*a) + (['0']*b)), base=2)
    m = int(''.join(['1'] + (['0']*b) + (['1']*(a - 1))), base=2)
    print(f'#{case} {(bin((M*m)).count(str(1)))}')
