import sys 
input = sys.stdin.readline

from typing import List

def mean(a: List[int]) -> int:
    return int(round(sum(a)/len(a), 0))

def median(a: List[int]) -> int:
    return sorted(a)[(len(a))//2]

def mode(a: List[int]) -> int:
    cnt = {}
    for x in a:
        cnt[x] = 0 if cnt.get(x) == None else cnt[x] + 1
    
    m_k = []
    m_v = max(cnt.values())
    for k in cnt.keys():
        if cnt[k] == m_v:
            m_k.append(k)
    
    return m_k[0] if len(m_k) == 1 else sorted(m_k)[1]

def rnge(a: List[int]) -> int:
    return max(a) - min(a)


n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

print(mean(a))
print(median(a))
print(mode(a))
print(rnge(a))
