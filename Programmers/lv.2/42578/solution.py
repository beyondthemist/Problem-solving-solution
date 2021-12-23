# https://programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    dic = {}

    for i in range(len(clothes)):
        li = clothes[i]
        
        if li[-1] in dic:
            dic[li[-1]] = dic[li[-1]] + len(li) - 1
        else:
            dic[li[-1]] = len(li) - 1 
    
    count = 1
    li = list(dic.keys())
    for i in li:
        count = count * (dic.get(i) + 1)
    
    return (count - 1)
