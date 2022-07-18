from math import sqrt

t = int(input())
a = []
for i in range(t):
    a.append(int(input()))

m = max(a)
is_prime = [False] + [True for i in range(m - 1)]
for i in range(1, int(sqrt(m)) + 1):
    if is_prime[i]:
        for j in range(i + (i + 1), m, i + 1):
            is_prime[j] = False

for x in a:
    for j in range(x//2, 1, -1):
        if is_prime[j - 1] and is_prime[x - j - 1]:
            print(j, x - j)
            break
