#https://programmers.co.kr/learn/courses/30/lessons/12977

from math import sqrt

def solution(nums):
    is_prime = [True for i in range(0, sum(sorted(nums)[-3:]) + 1)]
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(sqrt(len(is_prime))) + 1):
        if is_prime[i]:
            for j in range(2*i, len(is_prime), i):
                is_prime[j] = False
    
    
    answer = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                temp = nums[i] + nums[j] + nums[k]
                if is_prime[temp]:
                    answer += 1
                
    print(is_prime)
    return answer

