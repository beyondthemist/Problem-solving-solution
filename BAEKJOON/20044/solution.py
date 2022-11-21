import sys 
input = sys.stdin.readline

n = int(input())
a = sorted([int(x) for x in input().split()])
a = [(a[i] + a[-(i + 1)]) for i in range(n)]
print(min(a))
