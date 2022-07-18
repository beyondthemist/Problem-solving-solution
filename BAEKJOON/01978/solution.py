# https://www.acmicpc.net/problem/1978

def is_prime(x):
    if x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        for i in range(2, x):
            if x%i == 0:
                return 0
    return 1


n = int(input())
count = 0
for s in input().split():
    count += is_prime(int(s))
print(count)
