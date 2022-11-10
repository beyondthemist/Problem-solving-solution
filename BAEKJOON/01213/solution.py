import sys 
input = sys.stdin.readline

name = input().rstrip()
res = []
d = {}
for c in range(ord('A'), ord('Z') + 1):
    d[chr(c)] = 0

for c in name:
    d[c] += 1

count_odd = 0
for c in d.keys():
    if d[c]%2 != 0:
        count_odd += 1

if count_odd > 1:
    print('I\'m Sorry Hansoo')
else:
    remainder = ''
    for k in sorted(d.keys()):
        while d[k] > 1:
            res.append(k)
            d[k] -= 2

        if d[k] == 1:
            remainder = k

    print(''.join(res + [remainder] + sorted(res, reverse=True)))
