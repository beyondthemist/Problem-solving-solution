# https://www.acmicpc.net/problem/1157
d = {}
for c in input().upper():
    d[c] = (d[c] + 1 if c in d.keys() else 1)

m = max(d.values())
res = None
for key in d.keys():
    if d[key] == m:
        if res == None:
            res = key
        else:
            res = '?'
            break
print(res)
