import sys
input = sys.__stdin__.readline

n, m = [int(x) for x in input().split()]
p, q = [], []
for _ in range(m):
    price = input().split()
    p.append(int(price[0]))
    q.append(int(price[1]))

m = 1000*n
for p1 in p:
    for p2 in q:
        temp = min((n//6)*p1 + (n%6)*p2, (n//6 + 1)*p1, n*p2)
        if m > temp:
            m = temp

print(m) 
