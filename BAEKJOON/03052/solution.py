import sys
input = sys.__stdin__.readline

a = [0 for _ in range(42)]
for _ in range(10):
    a[int(input())%42] += 1

count = 0
for x in a:
    if x > 0:
        count += 1

print(count)
