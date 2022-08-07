import sys
sys.setrecursionlimit(10 ** 5) # RecursionError may occur if limit is default(10 ** 3)

def count(acre):
    def search(acre, x, y):
        if  x < 0 or len(acre) <= x \
            or y < 0 or len(acre[x]) <= y \
            or acre[x][y] != 1:
            return

        acre[x][y] = 2
        search(acre, x - 1, y)
        search(acre, x + 1, y)
        search(acre, x, y - 1)
        search(acre, x, y + 1)

    count = 0
    for i in range(len(acre)):
        for j in range(len(acre[i])):
            if acre[i][j] == 1:
                search(acre, i, j)
                count += 1
    return count

t = int(input())
for i in range(t):
    m, n, k = [int(x) for x in input().split()]
    acre = [[0 for cols in range(m)] for rows in range(n)]
    
    for j in range(k):
        x, y = [int(a) for a in input().split()]
        acre[y][x] = 1

    print(count(acre))
