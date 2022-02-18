# https://programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    s = [int(x) for x in s.split()]
    return str(min(s)) + ' ' + str(max(s))
