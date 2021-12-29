# https://programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    n = list(str(n))
    n.reverse()
    answer = [int(i) for i in n]
    
    return answer
