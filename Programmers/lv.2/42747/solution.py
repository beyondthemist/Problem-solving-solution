# https://programmers.co.kr/learn/courses/30/lessons/42747

import numpy as np

def solution(citations):
    a = np.array(citations)
    
    answer = 0
    for h in range(max(citations), -1, -1):
        if np.size(a[a >= h]) >= h:
            answer = h
            break
    
    return answer
