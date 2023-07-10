from math import ceil, floor, sqrt

def solution(r1, r2):
    answer = 2*(r2 - r1 + 1)
    
    for x in range(1, r1):
        answer += 4*(floor(sqrt((r2**2) - (x**2))) - ceil(sqrt((r1**2) - (x**2))) + 1)
    
    for x in range(r1, r2 + 1):
        answer += 2*(2*(floor(sqrt((r2**2) - (x**2)))) + 1)

    return answer
