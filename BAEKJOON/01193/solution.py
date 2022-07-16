# https://www.acmicpc.net/problem/1193

def sum(n):
    return (n*(n + 1))//2

x = int(input())

n = 1
while sum(n) < x:
    n += 1

diff = x - sum(n - 1) - 1
if n%2 == 0: # ↙
    print(f'{1 + diff}/{n - diff}')
else: # ↗
    print(f'{n - diff}/{1 + diff}')
