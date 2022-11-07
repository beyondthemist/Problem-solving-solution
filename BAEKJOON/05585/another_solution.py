import sys 
input = sys.stdin.readline

n = int(input())
n = 1000 - n
yens = [500, 100, 50, 10, 5, 1]

count = 0 
idx = 0
while n != 0:
    if yens[idx] > n:
        idx += 1
    else:
        n -= yens[idx]
        count += 1
print(count)
