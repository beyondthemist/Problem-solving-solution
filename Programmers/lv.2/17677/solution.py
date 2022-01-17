# https://programmers.co.kr/learn/courses/30/lessons/17677 

# J(A, B) = n(A and B) / n(A or B)
def j(a, b):
    i = u = 0
    for e in (set(a)).union(set(b)):
        i += min(a.count(e), b.count(e)) #n(A ∩ B)
        u += max(a.count(e), b.count(e)) #n(A ∪ B)
    
    return 1 if u == 0 else i / u

def get_set(s): #Multiple set
    l = []
    for i in range(len(s) - 1):
        if (('a' <= s[i] and s[i] <= 'z')
            and ('a' <= s[i + 1] and s[i + 1] <= 'z')):
            l.append(s[i:i+2])
    return l

def solution(str1, str2):
    l1 = get_set(str1.lower())
    l2 = get_set(str2.lower())
    
    return int(j(l1, l2) * 65536)
