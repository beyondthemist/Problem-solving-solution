# https://programmers.co.kr/learn/courses/30/lessons/12922

def solution(n):
    return ''.join(['수' if i%2 == 0 else '박' for i in range(n)])
