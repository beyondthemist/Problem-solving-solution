# https://programmers.co.kr/learn/courses/30/lessons/77884

def solution(left, right):
    squares = set([x**2 for x in range(1, right + 1)])
    answer = sum([(-n if n in squares else n) for n in range(left, right + 1)])
    return answer

#solution = lambda left, right: sum(-n if int(n**0.5) == n**0.5 else n for n in range(left, right + 1))
