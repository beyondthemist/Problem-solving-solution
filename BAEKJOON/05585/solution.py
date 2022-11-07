import sys 
input = sys.stdin.readline

n = int(input())
n = 1000 - n
yens = [500, 100, 50, 10, 5, 1]

count = 0 
for yen in yens:
    count += (n//yen)
    n %= yen
print(count)
