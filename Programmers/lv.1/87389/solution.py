#https://programmers.co.kr/learn/courses/30/lessons/87389

def solution(n):
    if n%2 == 1:
        answer = 2 
    else:
        i = 3
        while n%i != 1:
            i += 1
        answer = i
    return answer
