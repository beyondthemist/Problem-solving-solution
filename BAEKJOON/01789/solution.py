s = int(input())
n = 1
summation = 0
while n <= s - summation:
    summation += n
    n += 1
print(n - 1)
