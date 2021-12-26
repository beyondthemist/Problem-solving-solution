# https://programmers.co.kr/learn/courses/30/lessons/12977
from math import sqrt
from itertools import combinations

def solution(nums):
    is_prime = [True for i in range(0, sum(sorted(nums)[-3:]) + 1)]
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(sqrt(len(is_prime))) + 1):
        if is_prime[i]:
            for j in range(2*i, len(is_prime), i):
                is_prime[j] = False
    
    answer = 0
    for c in combinations(nums, 3):
        if is_prime[sum(c)]:
            answer += 1
            
    return answer
