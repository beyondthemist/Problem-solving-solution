n = int(input())
ss = [list(input()) for _ in range(n)]
for i in range(1, n):
    for j in range(len(ss[i])):
        if ss[i - 1][j] != ss[i][j]:
            ss[i][j] = '?'

print(''.join(ss[-1]))
