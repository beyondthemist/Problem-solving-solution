# https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = [0 for i in prices]
    
    for i in range(len(prices) - 1):
        idx = i + 1
        while idx < len(prices) - 1 and prices[idx] >= prices[i]:
            idx += 1    
        answer[i] = idx - i

    return answer
