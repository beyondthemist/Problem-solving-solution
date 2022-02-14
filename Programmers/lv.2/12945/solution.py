# https://programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    x, y = 0, 1
    for i in range(n - 1):
        x, y = y, x + y

    return y % 1234567
