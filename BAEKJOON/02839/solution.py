n = int(input())

count = 0
while n%5 != 0:
    count += 1
    n -= 3

print(-1 if n < 0 else n//5 + count)
