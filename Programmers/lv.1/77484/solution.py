#https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    matches = 0
    zeros = 0
    for num in lottos:
        if num in win_nums:
            matches = matches + 1
        elif num == 0:
            zeros = zeros + 1
    
    M = min(6 - (matches + zeros) + 1, 6)
    m = min(6 - matches + 1, 6)
    
    answer = [M, m]
    return answer
