# https://www.acmicpc.net/problem/11047

n, k = [int(x) for x in input().split()]
coins = []
for i in range(n):
    coins.insert(0, int(input()))

count = 0
for x in coins:
    count += k//x
    k %= x
print(count)
