t = int(input())
a = [1, 2, 4]

n = []
for i in range(t):
    n.append(int(input()))

for i in range(3, max(n)):
    a.append(a[i - 1] + a[i - 2] + a[i - 3])

for x in n:
    print(a[x - 1])
