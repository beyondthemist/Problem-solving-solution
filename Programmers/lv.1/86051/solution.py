# https://programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers):
    answer = sum(range(0,10)) - sum(numbers)
    return answer
