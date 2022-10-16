n = 600851475143
i = 3
while i*i <= n:
    while n%i == 0:
        n //= i
    i += 2

print(n)
