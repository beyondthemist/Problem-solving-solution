#https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer = []
    for m in range(yellow + 2, 0, -1):
        n = (brown + yellow)//m
        
        if 2*(m+n) - 4 == brown and (m-2)*(n-2) == yellow:
            answer = [m, n]
            break
            
    return answer
