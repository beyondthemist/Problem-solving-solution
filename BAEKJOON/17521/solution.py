import sys 
input = sys.stdin.readline

n, w = [int(x) for x in input().split()]
prices = []
for _ in range(n):
    prices.append(int(input()))

coins = 0
for i in range(0, n - 1):
    if prices[i] < prices[i + 1]:
        if w >= prices[i]:
            coins = w//prices[i]
            w %= prices[i]
    elif prices[i] > prices[i + 1]:
        w += coins*prices[i]
        coins = 0

w += coins*prices[-1]

print(w)
