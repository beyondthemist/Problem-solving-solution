t = int(input())

for test_case in range(1, t + 1):
    board = [[int(x) for x in input().split()] for _ in range(9)]
    legal = True
    # check_row
    for i in range(9):
        if len(set(board[i])) < 9:
            legal = False
            break

    if not legal:
        print(f'#{test_case} 0')
        continue

    # check_column
    for j in range(9):
        col = [board[i][j] for i in range(9)]
        if len(set(col)) < 9:
            legal = False
            break

    if not legal:
        print(f'#{test_case} 0')
        continue

    # check_subsquare
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            temp = []
            for k in range(3):
                for l in range(3):
                    temp.append(board[i+k][j+l])
            if len(set(temp)) < 9:
                legal = False
                break

        if not legal:
            break

    print(f'#{test_case} {int(legal)}')
