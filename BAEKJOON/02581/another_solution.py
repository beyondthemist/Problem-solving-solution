# https://www.acmicpc.net/problem/2581

m, n = int(input()), int(input())
is_prime = [0] + [i + 2 for i in range(n - 1)]

i = 1
while i*i <= n:
    if is_prime[i] != 0:
        for j in range(2*i + 1, n, (i + 1)):
            is_prime[j] = 0
    i += 1

i = n + 1
s = 0
for x in is_prime[(m - 1):n]:
    if x != 0:
        s += x
        if i > x:
            i = x
if s == 0:
    print(-1)
else:
    print(s)
    print(i)
