#https://programmers.co.kr/learn/courses/30/lessons/70128

def solution(a, b):
    answer = 0
    for x, y in zip(a, b):
        answer += x*y
        
    return answer

#solution = lambda a, b: sum([x*y for x, y in zip(a, b)])
