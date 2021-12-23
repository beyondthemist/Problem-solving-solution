# https://programmers.co.kr/learn/courses/30/lessons/64061
def solution(board, moves):
    basket = [0, ]
    count = 0
    for move in moves:
        picked = 0
        for row in range(len(board)):
            if board[row][move - 1] != 0:
                picked = board[row][move - 1]
                board[row][move - 1] = 0           
                break
                
        if picked != 0:
            if picked == basket[-1]:
                del basket[-1]
                count = count + 2
            else:
                basket.append(picked)
    
    answer = count
    return answer
