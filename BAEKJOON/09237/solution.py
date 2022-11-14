import sys 
input = sys.stdin.readline

n = int(input())
t = sorted([int(x) for x in input().split()])
t = [max(t[i] - i, 0) for i in range(n)]

print(max(t) + 1 + n)
