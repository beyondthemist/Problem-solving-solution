import sys 
input = sys.stdin.readline

n = int(input())
tips = sorted([int(input()) for _ in range(n)], reverse=True)
tips = [max(tips[i] - i, 0) for i in range(n)]

print(sum(tips))
