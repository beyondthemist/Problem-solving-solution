# https://programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    answer = min(len(set(nums)), len(nums)//2)
    return answer
