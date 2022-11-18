import sys 
input = sys.stdin.readline

n, m = [int(x) for x in input().split()]
lim = min(n, m)

prices = sorted([int(input()) for _ in range(m)], reverse=True)
max_revenue = 0
max_price = 0
for i in range(lim):
    revenue = (i + 1)*prices[i]
    if max_revenue < revenue:
        max_revenue = revenue
        max_price = prices[i]

print(f'{max_price} {max_revenue}')
