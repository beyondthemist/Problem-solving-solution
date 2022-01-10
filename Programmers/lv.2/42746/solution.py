#https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    if numbers.count(0) == len(numbers):
        return '0'
    
    numbers = [str(x) for x in numbers]
    return ''.join(sorted(numbers, key=lambda x: (x*4)[0:4], reverse=True))
