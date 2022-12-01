from typing import List
from collections import OrderedDict

def solution(k, tangerines: List[int]):
    if k == 1:
        return 1

    d = {}
    for key in set(tangerines):        
        d[key] = 0
    for tangerine in tangerines:
        d[tangerine] += 1
    d = OrderedDict(sorted(d.items(), key=lambda item: item[1], reverse=True)) 
    
    cnt = 0
    answer = 0
    for item in d.items():
        k -= item[1]
        answer += 1

        if k <= 0:
            break

    return answer
