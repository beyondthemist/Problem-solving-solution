import sys 
input = sys.stdin.readline

n = int(input())
prices = sorted([int(input()) for _ in range(n)], reverse=True)
print(sum(prices) - sum(prices[2:n:3]))
