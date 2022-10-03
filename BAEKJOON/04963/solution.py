import sys
input = sys.__stdin__.readline
sys.setrecursionlimit(10 ** 5)

def dfs(ground, i, j):
    if (i < 0 or j < 0) \
    or (len(ground) <= i or len(ground[i]) <= j):
        return

    if ground[i][j] != 1:
        return

    ground[i][j] = 2
    for a in [-1, 0, 1]:
        for b in [-1, 0, 1]:
            dfs(ground, i + a, j + b)


w, h = [int(x) for x in input().split()]
while w != 0 and h != 0:
    count = 0
    ground = []
    for _ in range(h):
        ground.append([int(c) for c in input().split()])
    

    for i in range(h):
        for j in range(w):
            if ground[i][j] == 1:
                dfs(ground, i, j)
                count += 1
    print(count)
    
    w, h = [int(x) for x in input().split()]
