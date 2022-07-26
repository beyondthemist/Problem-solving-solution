# https://www.acmicpc.net/problem/3009

x, y = [], []
for _ in range(3):
    s = input().split()
    x.append(s[0])
    y.append(s[1])

for p in x:
    if x.count(p) <= 1:
        x.append(p)
        break

for q in y:
    if y.count(q) <= 1:
        y.append(q)
        break

print(f'{x[-1]} {y[-1]}')
