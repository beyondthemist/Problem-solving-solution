# https://programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    stack = []
    for x in s:
        stack.append(x)
        if stack[-2:] == ['(', ')']:
            del stack[-2:]

    return len(stack) == 0
