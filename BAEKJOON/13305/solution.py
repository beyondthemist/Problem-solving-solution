# https://www.acmicpc.net/problem/13305

n = int(input())
d = [int(x) for x in input().split()]
price = [int(x) for x in input().split()]
m, m_idx = price[0], 0
cost = 0
for i in range(1, n - 1):
    if m >= price[i]:
        cost += m*(sum(d[m_idx:i]))
        m = price[i]
        m_idx = i
cost += m*(sum(d[m_idx:(n - 1)]))
print(cost)
