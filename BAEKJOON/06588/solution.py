def get_goldbach_pair(n, sieve):
    for b in range(2, n//2 + 1):
        if sieve[n - b] and sieve[b]:
            return f'{n} = {b} + {n - b}'

    return 'Goldbach\'s conjecture is wrong.'


n = int(input())
i = []
while n != 0:
    i.append(n)
    n = int(input())

m = max(i)
sieve = [False, False, True] + [True]*(m - 2) #is_prime
idx = 2
while idx*idx <= m:
    if sieve[idx]:
        for j in range(idx << 1, m, idx):
            sieve[j] = False
    idx += 1

for x in i:
    print(get_goldbach_pair(x, sieve))
