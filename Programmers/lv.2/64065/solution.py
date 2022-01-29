#https://programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    s = s[2:-2].split('},{')
    s.sort(key=lambda x: len(x))

    answer = []
    for x in s:
        for i in [int(y) for y in x.split(',')]:
            if i not in answer:
                answer.append(i)
    
    return answer
