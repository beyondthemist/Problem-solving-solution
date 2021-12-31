# https://programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    s = s.split(' ')
    
    for i in range(len(s)):
        x = list(s[i])
        
        for j in range(len(x)):
            x[j] = x[j].upper() if j%2 == 0 else x[j].lower()
        
        s[i] = ''.join(x)
        
    return ' '.join(s)
