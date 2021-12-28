# https://programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    answer = s[len(s)//2 if len(s)%2 == 1 else len(s)//2-1:len(s)//2+1 ]
    return answer
