import sys
input = sys.__stdin__.readline

c = int(input())
for _ in range(c):
    a = [int(x) for x in input().split()]
    avg = sum(a)//(int(a[0]))
    count = 0
    for x in a[1:]:
        if x >= avg:
            count += 1
    print('{:.3f}%'.format(round(count/a[0]*100, 3)))
