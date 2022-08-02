# https://www.acmicpc.net/problem/1018

def count(board, x1, x2, y1, y2):
    count1 = 0
    count2 = 0
    for i in range(x1, x2):
        for j in range(y1, y2):
            if (i + j)%2 == 0:
                if board[i][j] != 'W':
                    count1 += 1
                else:
                    count2 += 1
            else:
                if board[i][j] != 'B':
                    count1 += 1
                else:
                    count2 += 1

    return min(count1, count2)

h, w = [int(x) for x in input().split()]
board = [list(input()) for _ in range(h)]

m = h * w
for i in range(h - 7):
    for j in range(w - 7):
        c = count(board, i, i + 8, j, j + 8)
        if m > c:
            m = c 

print(m)
