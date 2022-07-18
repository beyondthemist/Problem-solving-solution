inputs = []
n = int(input())
while n != 0:
    inputs.append(n)
    n = int(input())

m = max(inputs)
is_prime = [0] + [1 for i in range(2*m - 1)]
i = 1
while i*i <= 2*m:
    if is_prime[i]:
        for j in range(2*i + 1, 2*m, (i + 1)):
            is_prime[j] = 0
    i += 1

for x in inputs:
    print(sum(is_prime[x:(2*x)]))        
