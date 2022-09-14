n, k = [int(x) for x in input().split()]
res = 1
for i in range(1, k + 1):
    res *= (n - i + 1) 
    res //= i

print(res%10007)
