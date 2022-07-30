# https://www.acmicpc.net/problem/2675

for _ in range(int(input())):
    tmp = input().split()
    r, s = int(tmp[0]), tmp[1]
    res = []
    for c in s:
        for i in range(r):
            res.append(c)
    print(''.join(res))
