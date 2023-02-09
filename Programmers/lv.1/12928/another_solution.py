# https://programmers.co.kr/learn/courses/30/lessons/12928

from math import sqrt

def solution(n):
    s = 0
    i = 1
    end = sqrt(n)
    while i <= end:
        if n%i == 0:
            s += (i + (n//i)) if i != n//i else i
        i += 1
    
    return s
