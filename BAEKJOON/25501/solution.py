import sys
input = sys.__stdin__.readline

t = int(input())
for _ in range(t):
    s = input()
    l, r = 0, (len(s) - 2) # readline() include '\n'
    count = 0
    res = 1
    while True:
        count += 1
        if l >= r:
            break
        if s[l] != s[r]:
            res = 0
            break
        l += 1
        r -= 1

    print(res, count)
