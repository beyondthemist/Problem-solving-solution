# https://programmers.co.kr/learn/courses/30/lessons/77884

#from math import sqrt

def solution(left, right):
    #squares = [x**2 for x in range(1, int(sqrt(right)) + 1)]
    squares = [x**2 for x in range(1, right + 1)]
    answer = sum([(-n if n in squares else n) for n in range(left, right + 1)])
    return answer
