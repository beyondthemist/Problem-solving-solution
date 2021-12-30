# https://programmers.co.kr/learn/courses/30/lessons/12934

from math import sqrt

def solution(n):
    x = sqrt(n)
    return (int(x) + 1)**2 if x**2 == (int(x))**2 else -1
