from math import sqrt

def solution(k, d):
    return sum([((int(sqrt(d**2 - x**2))//k) + 1) for x in range(0, d + 1, k)])


'''
from math import sqrt

def solution(k, d):
    answer = 0
    
    for x in range(0, d + 1, k):
        answer += ((int(sqrt(d**2 - x**2))//k) + 1)
        
    return answer
'''
