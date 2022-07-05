# https://programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    d = {}
    for s in strings:
        if s[n] not in d.keys():
            d[s[n]] = [s, ]
        else:
            d[s[n]].append(s)
            
    for k in d.keys(): #sort words
        d[k].sort()
    
    answer = [word for words in sorted(d.items(), key = lambda x: x[0]) for word in words[1]]
    
    return answer
