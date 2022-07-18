# https://www.acmicpc.net/problem/2581

def is_prime(x):
    if x <= 1:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2, x):
            if x%i == 0:
                return False
    return True

m, n = int(input()), int(input())
minimum, count = n, 0
for x in range(m, n + 1):
    if is_prime(x):
        count += x
        if minimum > x:
            minimum = x

if count == 0: 
    print(-1)
else:
    print(count)
    print(minimum)
