# https://programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    d = sorted(d)
    i = 1
    while sum(d[:i]) <= budget and i <= len(d):
        i += 1
    
    answer = i - 1
    return answer
