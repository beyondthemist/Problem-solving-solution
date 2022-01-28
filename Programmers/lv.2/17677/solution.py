# https://programmers.co.kr/learn/courses/30/lessons/17677 

def j(a, b):
    i = u = 0
    for e in (set(a)).union(set(b)):
        i += min(a.count(e), b.count(e)) #n(A ∩ B)
        u += max(a.count(e), b.count(e)) #n(A ∪ B)
    
    return 1 if u == 0 else i / u

def get_set(s): #Multiple set
    l = []
    for i in range(len(s) - 1):
        #if (('a' <= s[i] and s[i] <= 'z')
        #    and ('a' <= s[i + 1] and s[i + 1] <= 'z')):
        if s[i].isalpha() and s[i + 1].isalpha():
            l.append(s[i:i+2])    
    return l

def solution(str1, str2):
    return int(j(get_set(str1.lower()), get_set(str2.lower())) * 65536)
