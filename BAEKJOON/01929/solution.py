# https://www.acmicpc.net/problem/1929

m, n = [int(x) for x in input().split()]
is_prime = [False] + [True for i in range(n - 1)]

# Construct Erathostenes' sieve
for i in range(1, n):
    if is_prime[i]:
        for j in range((2*i) + 1, n, i+1):
            is_prime[j] = False
    
#print
for i in range(m - 1, n):
    if is_prime[i]:
        print(i + 1)
