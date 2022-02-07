# https://programmers.co.kr/learn/courses/30/lessons/12985

def solution(n, a, b):
    answer = 1
    
    while not (abs(b - a) == 1 and min(a, b)%2 == 1):
        a, b = a//2 + a%2, b//2 + b%2
        answer += 1
    
    return answer
