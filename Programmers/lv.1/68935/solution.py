# https://programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    s = ''
    while n > 0:
        s += str(n%3)
        n //= 3
    answer = int(s, 3)
    return answer
