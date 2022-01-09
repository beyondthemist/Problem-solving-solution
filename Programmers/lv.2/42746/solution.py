#https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    if numbers == [0]*len(numbers):
        return '0'
    else:
        return ''.join(sorted([str(x) for x in numbers], key=lambda x: x*3, reverse=True))
